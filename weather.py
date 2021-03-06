import requests
from bs4 import BeautifulSoup
import pandas as pd
period_names = []
short_desc = []
temp = []
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=31.80967000000004&lon=-85.97216999999995#.XiN3XMhKhPY')
soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all(class_ = 'tombstone-container')

for item in items:
    period_names.append(item.find(class_='period-name').get_text())
    short_desc.append(item.find(class_='short-desc').get_text())
    temp.append(item.find(class_='temp').get_text())

weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short_descriptions': short_desc,
     'temperatures': temp,
     }
)

weather_stuff.to_csv('weather.csv')
print(weather_stuff)