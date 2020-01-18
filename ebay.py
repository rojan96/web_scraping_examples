import requests
from bs4 import BeautifulSoup
import pandas as pd
titles = []
ending_in = []
price = []
search=input("What do you wanna search for?")
page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+search+'&_sacat=0&LH_Auction=1&_sop=1&_ipg=200')
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='srp-results srp-list clearfix')

each_result = results.find_all(class_='s-item__wrapper clearfix')


for item in each_result:
    titles.append(item.find(class_="s-item__title").get_text())
    price.append(item.find(class_="s-item__price").get_text())
    ending_in.append(item.find(class_="s-item__time-left").get_text())

results_stuff = pd.DataFrame(
    {'Title':titles,
     'Ending in':ending_in,
     'Price':price,
     })
print(results_stuff)
results_stuff.to_csv('auction.csv')


print(titles[:5])
print(price[:5])
print(ending_in[:5])