from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
price_tracker = response.text

soup = BeautifulSoup(price_tracker, "html.parser")

price_element = soup.select_one(".aok-offscreen").getText()
price = price_element.split("$")[1]
price_as_float = float(price)
print(price_as_float)