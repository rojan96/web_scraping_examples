import requests
from bs4 import BeautifulSoup
import pandas as pd
titles = []
ending_in = []
price = []
search = input("What do you wanna search for?")
page = requests.get('https://www.amazon.com/s?k='+search+'&ref=nb_sb_noss_2')
soup = BeautifulSoup(page.content, 'html.parser')

each_result = soup.find_all(class_='sg-col-inner')

for item in each_result:
    title = item.find(class_='a-size-medium a-color-base a-text-normal')
    price_whole = item.find(class_="a-price-whole")
    price_fraction = item.find(class_="a-price-fraction")
    if title and price_whole and price_fraction:
        titles.append(title.get_text())
        price.append(price_whole.get_text() + price_fraction.get_text())

results_stuff = pd.DataFrame(
    {'Title':titles,
     'Price':price,
     })

print((results_stuff['Price']).mean())
# results_stuff.to_csv('amazon_prices.csv')
