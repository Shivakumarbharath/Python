from bs4 import BeautifulSoup
import requests

res=requests.get('https://en.wikipedia.org/wiki/Web_scraping')

soup=BeautifulSoup(res.text,'lxml')

print(soup.get_text().replace('\n\n',''))