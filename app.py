import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://coinmarketcap.com/"
conn_url = 'postgresql://{USERNAME}:{PASSWORD}@localhost:{NUMBER}/{DATABASE}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'cd2a1888f4437c1ebb7aae99763716363412bf3ce9ab2ad996f319851f2e27aa',
    'Priority': 'u=0, i',
    'Referer': 'https://coinmarketcap.com/',
    'Upgrade-Insecure-Requests': '1'
}

# Fetching the website
def get_website():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Successfully fetched the page!")
    else:
        raise Exception(f"Failed to fetch webpage: {r.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    if not table:
        raise Exception("Unable to locate the table on the page.")

    return table

# Locating and extract the table
def get_crypto_data():
    table = get_website()
    headers = [th.text.strip() for th in table.find_all("th")]
    rows = []

    for tr in table.find_all("tr"):
        cells = [td.text.strip() for td in tr.find_all("td")]

        if cells and len(rows) <= 5:
            rows.append(cells)
    
    df = pd.DataFrame(rows, columns=headers if headers else None)
    return df

# Extract the null columns 
def remove_null_columns():
    df = get_crypto_data()
    df = df.loc[:, df.columns.notnull()]
    df = df.loc[:, df.columns.str.strip() != '']
    return df

# Extract the unnessarily symbols
def clean_money_percent(val):
    if isinstance(val, str):
        val = val.replace('$', '').replace('%', '').replace(',', '').strip()
    return val

# Applying the clean money percent and adding to dataframe
def apply_clean_money_percent():
    df = remove_null_columns()
    df['Price'] = df['Price'].apply(clean_money_percent).astype(float)
    df['1h %'] = df['1h %'].apply(clean_money_percent).astype(float)
    df['24h %'] = df['24h %'].apply(clean_money_percent).astype(float)
    df['7d %'] = df['7d %'].apply(clean_money_percent).astype(float)
    return df

# Extract the last large number (after B/T prefix)
def clean_market_cap(val):
    matches = re.findall(r'([\d,]+)', val)
    if matches:
        number = matches[-1].replace(',', '')
        return float(number)
    else:
        return None

# Applying the clean market cap and adding to dataframe
def apply_clean_market_cap():
    df = apply_clean_money_percent()
    df['Market Cap'] = df['Market Cap'].apply(clean_market_cap)
    return df

# Extract the first large number (before token name)
def clean_volume(val):
    matches = re.findall(r'([\d,]+)', val)
    if matches:
        number = matches[0].replace(',', '')
        return float(number)
    else:
        return None

# Applying the clean volume and adding to dataframe
def apply_clean_volume():
    df = apply_clean_money_percent()
    df['Volume(24h)'] = df['Volume(24h)'].apply(clean_volume)
    return df

# Extract numeric part and unit
def clean_supply(val):
    match = re.match(r'([\d\.]+)([KMB]?)', val.strip())
    if match:
        number, unit = match.groups()
        number = float(number)
        if unit == 'K':
            number *= 1e3
        elif unit == 'M':
            number *= 1e6
        elif unit == 'B':
            number *= 1e9
        return number
    return None

# Applying the clean supply and adding to dataframe
def apply_clean_supply():
    df = apply_clean_volume()
    df['Circulating Supply'] = df['Circulating Supply'].apply(lambda x: clean_supply(x.split()[0]))
    return df

#Writing the dataframe to sql
def save_to_sql():
    df = apply_clean_supply()
    df_sql = df.to_sql('crypto_data',
                   conn_url,
                   if_exists='append',
                   index=False)

if __name__ == "__main__":
    pd.read_sql('crypto_data', conn_url)
