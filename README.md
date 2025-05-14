# Web Scraping Cryptocurrency Data from CoinMarketCap

This project demonstrates how to perform web scraping of real-time cryptocurrency data from [CoinMarketCap](https://coinmarketcap.com/) using Python. The goal is to extract the top cryptocurrency information from the homepage table, clean it, and store it in a sql database for further analysis.

## 📌 Features

- Scrapes the top-listed cryptocurrencies from CoinMarketCap
- Extracts key data fields such as:
  - Name
  - Symbol
  - Price
  - Market Cap
  - 24h Volume
  - % Change (24h, 7d)
- Cleaned the data by removing unwanted symbols and null columns.
- Saves data to sql database
- Includes logging and error handling
- Modular and easy to extend for other pages or data points

## 🛠️ Tools & Technologies Used

- Python 3.x
- `requests` – for sending HTTP requests
- `BeautifulSoup` (bs4) – for parsing HTML content
- `pandas` – for data structuring and saving