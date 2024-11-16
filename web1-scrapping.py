import pandas as pd
import requests
from bs4 import BeautifulSoup

# Proxy settings
proxies = {
    "http": "http://pawucgmo-rotate:0xwu5423a2mp@p.webshare.io:80/",
    "https": "http://pawucgmo-rotate:0xwu5423a2mp@p.webshare.io:80/",
}

# Data structure for storing titles and prices
data = {'Title': [], 'Price': []}

# Amazon URL and headers
url = "https://www.amazon.in/s?k=s24&crid=1B30VGEG53N7A&sprefix=s2%2Caps%2C1073&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Making the request with headers and proxies
try:
    r = requests.get(url, headers=headers, proxies=proxies)
    r.raise_for_status()  # Check for request errors

    # Parsing the page
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.select("span.a-size-medium.a-color-base.a-text-normal")
    prices = soup.select("span.a-price-whole")

    # Extracting and storing the data
    for title in titles:
        data["Title"].append(title.get_text(strip=True))

    for price in prices[:len(data["Title"])]:  # Match number of titles and prices
        data["Price"].append(price.get_text(strip=True))

    # Saving data to CSV
    df = pd.DataFrame.from_dict(data)
    df.to_csv("data.csv", index=False)
    print("Data saved to data.csv")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
