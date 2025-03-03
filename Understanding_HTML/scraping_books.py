import requests
from bs4 import BeautifulSoup
page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
books = soup.find_all('article')
