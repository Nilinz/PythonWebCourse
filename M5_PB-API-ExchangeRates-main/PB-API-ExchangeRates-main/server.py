import asyncio
import logging
import websockets
import names
import datetime
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK
import aiohttp
from aiofile import async_open

import aiofile  # Додали імпорт aiofile

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            if message.startswith('exchange'):
                await self.handle_exchange_command(ws, message)
            else:
                await self.send_to_clients(f"{ws.name}: {message}")

    async def handle_exchange_command(self, ws: WebSocketServerProtocol, command: str):
        try:
            parts = command.split()
            if len(parts) == 1:
                days = 1
            else:
                days = int(parts[1])

            exchange_rates = await self.get_exchange_rates_last_days(days)
            await self.write_exchange_log(exchange_rates, ws.name)

            formatted_rates = self.format_exchange_rates(exchange_rates)

            await ws.send(formatted_rates)
        except ValueError:
            await ws.send("Невірний формат команди exchange. Використовуйте 'exchange <дні>' для перегляду курсів валют.")
        except Exception as e:
            print(f"Помилка обробки команди exchange: {e}")
            await ws.send("Помилка обробки команди exchange")

    async def get_exchange_rates_last_days(self, days: int):
        async with aiohttp.ClientSession() as session:
            today = datetime.date.today()
            dates = [(today - datetime.timedelta(days=i)).strftime("%d.%m.%Y") for i in range(days)]
            exchange_rates = []
            for date in dates:
                url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
                async with session.get(url) as response:
                    data = await response.json()
                    exchange_rates.append(data)
            return exchange_rates

    async def write_exchange_log(self, exchange_rates: list, user_name: str):
        log_filename = 'exchange_log.txt'
        async with async_open(log_filename, 'a') as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await log_file.write(f"Timestamp: {timestamp}, User: {user_name}\n")
            for rates in exchange_rates:
                await log_file.write(f"{rates}\n")
            await log_file.write("\n")

    def format_exchange_rates(self, exchange_rates: list):
        formatted_rates = []
        for rates in exchange_rates:
            date = rates['date']
            currencies = rates['exchangeRate']
            formatted_rate = f"Курс валют на {date}:\n"
            for currency in currencies:
                currency_name = currency['currency']
                purchase_rate = currency['purchaseRate']
                sale_rate = currency['saleRate']
                formatted_rate += f"{currency_name}: Покупка - {purchase_rate}, Продаж - {sale_rate}\n"
            formatted_rates.append(formatted_rate)
        return '\n'.join(formatted_rates)

async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
