# pip install requests
# py install requests
import requests

# response = requests.get('https://mail.ru')
# print(response)
API_key = "4321a3d417b53045aa1b6617c529c910" # 19163594b9bffd1c84a612b397714def"
#4321a3d417b53045aa1b6617c529c910

city_name = "Moscow"

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru")

print(response.json())

temp = response.json()
temp1 = temp["main"]
print(temp1["temp"])

from bs4 import BeautifulSoup as bs

# pip install bs4
#c_page = soup_data.find('div', class_='bx-pagination-container').find('ul').find_all('li')[5].find('a').find('span')
wheather = soup.find('div', class_='bx-pagination-container').find('ul').find_all('li')[5].find('a').find('span')

