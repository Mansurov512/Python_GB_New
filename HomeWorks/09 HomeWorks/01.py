# Написать простой парсер для извлечения информации с любого сайта.
# Например - новость, или погоду с сайта mail.ru

import requests
from bs4 import BeautifulSoup as bs

url = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/'
response = requests.get(url).text
# print(response)
soup = bs(response, "html.parser")
temperature = soup.find('div', "information__content__temperature") # парсим температуру
date_today = soup.find('div', "information__header__left__date") # парсим сегодняшний день с датой и временем
wheather_in_city = soup.find('h1', "information__header__left__place__city") # парсим фразу "Прогноз погоды в Санкт-Петербурге" просто из интереса, она статична

print(wheather_in_city.text)
print(date_today.text.strip())# парсит с кучей пробелов и переносов, потому обрезаю их с обоих сторон
print(temperature.text.strip()) # парсит с кучей пробелов и переносов, потому обрезаю их с обоих сторон



# pressue = soup.find('span', "information__content__additional__item__pressure") # парсим фразу "Прогноз погоды в Санкт-Петербурге" просто из интереса, она статична
# pressue1 = soup.find('span', "icon icon_preasure icon_mr-4") #
# pressue2 = soup.find('span', title="Давление: 746 мм рт. ст. пониженное") #
# pressue3 = soup.find('div', "information__content__additional__item").find(text="мм") #

# print(pressue)
# print(pressue1)
# print(pressue2.text)
# print(pressue3.text)

# body > div.g-layout.layout.layout_banner-side.js-module.js-adv-marker > div:nth-child(2) > div.block.block_forecast.block_index.forecast-rb-bg > div > div.information.block.js-city_one > div.information__content > div.information__content__wrapper.information__content__wrapper_left > a > div.information__content__additional.information__content__additional_second > div:nth-child(1) > span > span.icon.icon_preasure.icon_mr-4
# body > div.g-layout.layout.layout_banner-side.js-module.js-adv-marker > div:nth-child(2) > div.block.block_forecast.block_index.forecast-rb-bg > div > div.information.block.js-city_one > div.information__content > div.information__content__wrapper.information__content__wrapper_left > a > div.information__content__additional.information__content__additional_second > div:nth-child(1) > span > span.information__content__additional__item__pressure
# body > div.g-layout.layout.layout_banner-side.js-module.js-adv-marker > div:nth-child(2) > div.block.block_forecast.block_index.forecast-rb-bg > div > div.information.block.js-city_one > div.information__content > div.information__content__wrapper.information__content__wrapper_left > a > div.information__content__additional.information__content__additional_second > div:nth-child(1) > span


# body > div.g-layout.layout.layout_banner-side.js-module.js-adv-marker > div:nth-child(2) > div.block.block_forecast.block_index.forecast-rb-bg > div > div.information.block.js-city_one > div.information__header > div.information__header__left > div.information__header__left__date
# weather-icon weather-icon_size-80 weather-icon_31 weather-icon_31_size-80 weather-icon_mr-10
# information__content__temperature
# wheather = soup.find('div', class_='bx-pagination-container').find('ul').find_all('li')[5].find('a').find('span')
# print(soup)
#<div class="information__content__temperature">
# 	<span class="weather-icon weather-icon_size-80 weather-icon_03 weather-icon_03_size-80 weather-icon_mr-10" title="облачность" deluminate_imagetype="unknown"></span>+2°
# </div>

# /html/body/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/a/div[1]/div[1]/text()
# /html/body/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/a/div[1]/div[1]/text()
# +2°
# +2°

# <div class="information__content__temperature">
# 								<span class="weather-icon weather-icon_size-80 weather-icon_03 weather-icon_03_size-80 weather-icon_mr-10" title="облачность" deluminate_imagetype="unknown"></span>+2°
# 							</div>