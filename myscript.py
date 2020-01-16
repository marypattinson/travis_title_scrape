from bs4 import BeautifulSoup
import requests

url = r'https://www.bbc.co.uk/news'
r    = requests.get(url)

tag        = 'title' # find titles
title_soup = soup.find(tag)

title = title_soup.string
print(title)
