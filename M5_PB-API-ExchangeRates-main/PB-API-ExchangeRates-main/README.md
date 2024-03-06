# PB-API-ExchangeRates

This project has two main functionalities: fetching currency exchange rates from the PrivatBank API (currency.py) and creating a WebSocket chat server (server.py) along with a client interface (index.html). Additionally, there is a JavaScript file (main.js) for handling client-side interactions in the WebSocket chat.

## currency.py

- currency.py - fetching currency exchange rates from the PrivatBank API.
- supports fetching rates for up to 10 recent days.
- you can specify the currencies they want to fetch, with the default being EUR and USD.
- fetched data is saved to a JSON file with customizable output file name (default: currency_rates.json).

### Usage

Open a terminal or command prompt and navigate to the project directory.

Run the currency exchange rates script with the following command:

```
python currency.py <days> [--currencies CURRENCY [CURRENCY ...]] [--output OUTPUT_FILENAME]
```

--``currencies``: Specify a list of currencies to fetch (default: EUR and USD).

--``output``: Specify the output JSON file name (default: currency_rates.json).

Example:

```
python currency.py 5 --currencies EUR USD GBP --output rates.json
```
The script will fetch the currency exchange rates and save them to the specified JSON file.

## Running the WebSocket Chat Server

Run the WebSocket chat server with the following command:

```
python server.py
```

The server will start and listen for WebSocket connections on ws://localhost:8080.

## Running the WebSocket Chat

- Open the index.html file in a web browser.
 -In the web page, you can type a message in the text input field and click "Send message" to send it to the WebSocket server.


### Exchange Command

If a message starts with exchange, the server extracts the number of days specified in the command and fetches currency exchange rates from the PrivatBank API for the specified number of recent days.

```
exchange <days>
```

Exchange rates are logged to the exchange_log.txt file, along with a timestamp and the user's name who initiated the command.



