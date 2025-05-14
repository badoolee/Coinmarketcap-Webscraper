# Web Scraping Cryptocurrency Data from CoinMarketCap

This project demonstrates how to perform web scraping of real-time cryptocurrency data from [CoinMarketCap](https://coinmarketcap.com/) using Python. The goal is to extract the top cryptocurrency information from the homepage table, clean it, and store it in Postgresql for further analysis.

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
- Saves data to Postgresql
- Includes logging and error handling
- Modular and easy to extend for other pages or data points

## 🛠️ Tools & Technologies Used

- Python 3.x
- `requests` – for sending HTTP requests
- `BeautifulSoup` (bs4) – for parsing HTML content
- `pandas` – for data structuring and saving

# 🪙 Web Scraping Cryptocurrency Data from CoinMarketCap

This project demonstrates how to perform web scraping of real-time cryptocurrency data from [CoinMarketCap](https://coinmarketcap.com/) using Python. The goal is to extract the top cryptocurrency information from the homepage table, clean it, and store it in a structured format such as CSV or JSON for further analysis.

## 📌 Features

- Scrapes the top-listed cryptocurrencies from CoinMarketCap
- Extracts key data fields such as:
  - Name
  - Symbol
  - Price
  - Market Cap
  - 24h Volume
  - % Change (24h, 7d)
- Saves data to CSV or JSON
- Includes logging and error handling
- Modular and easy to extend for other pages or data points

## 🛠️ Tools & Technologies Used

- Python 3.x
- `requests` – for sending HTTP requests
- `BeautifulSoup` (bs4) – for parsing HTML content
- `pandas` – for data structuring and saving
- `lxml` – for efficient HTML parsing (optional but recommended)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/badoolee/Coinmarketcap-Webscraper.git
   cd coinmarketcap-webscraper

2. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

## How to Use
Ensure that you have set up your Postgresql database and input your USERNAME, PASSWORD, NUMBER, DATABASE.

```bash
  python scrape_coinmarketcap.py

This will fetch the latest data and display it.
