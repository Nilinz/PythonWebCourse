import argparse
import aiohttp
import asyncio
import json
import datetime

API_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="


async def fetch_exchange_rates(session, date):
    async with session.get(API_URL + date) as response:
        if response.status == 200:
            data = await response.json()
            return date, data.get("exchangeRate")
        else:
            raise Exception(f"Failed to fetch data for date {date}")


async def get_currency_rates(dates, currencies):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_exchange_rates(session, date) for date in dates]
        results = await asyncio.gather(*tasks)

        currency_rates = []
        for date, rates in results:
            if rates:
                currency_data = {}
                for rate in rates:
                    currency = rate["currency"]
                    sale_rate = rate.get("saleRate")
                    purchase_rate = rate.get("purchaseRate")
                    if sale_rate is not None and purchase_rate is not None:
                        currency_data[currency] = {"sale": sale_rate, "purchase": purchase_rate}
                currency_rates.append({date: currency_data})

        return currency_rates


def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Get currency exchange rates from PrivatBank API and save to a file.")
    parser.add_argument("days", type=int, help="Number of recent days to fetch rates for (up to 10)")
    parser.add_argument("--currencies", nargs="+", default=["EUR", "USD"], help="List of currencies to fetch (default: EUR USD)")
    parser.add_argument("--output", default="currency_rates.json", help="Output JSON file name (default: currency_rates.json)")
    args = parser.parse_args()

    if args.days > 10:
        print("Error: You can fetch rates for up to 10 days only.")
        return

    # Generate a list of dates for the last 'args.days' days
    today = datetime.date.today()
    dates = [(today - datetime.timedelta(days=i)).strftime("%d.%m.%Y") for i in range(args.days)]

    currency_rates = asyncio.run(get_currency_rates(dates, args.currencies))
    save_to_file(currency_rates, args.output)
    print(f"Currency rates saved to {args.output}.")


if __name__ == "__main__":
    main()
