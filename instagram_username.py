import requests
from bs4 import BeautifulSoup
username = input("Enter username to find real name")
page = requests.get('http://www.instagram.com/' + username + '')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('title').get_text().split("(")[0])
