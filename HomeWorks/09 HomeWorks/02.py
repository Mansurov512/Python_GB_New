# Написать простой парсер для извлечения информации с любого сайта.
# Например - новость, или погоду с сайта mail.ru

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.banki.ru/products/currency/cash/usd/sankt-peterburg/' # https://beta.gismeteo.ru
response = requests.get(url).text
# print(response)
soup = bs(response, "html.parser")
exchange = soup.find('div', "currency-table__large-text") # курс валюты

print(f"Курс ЦБ {exchange.text} рубля за доллар США.")