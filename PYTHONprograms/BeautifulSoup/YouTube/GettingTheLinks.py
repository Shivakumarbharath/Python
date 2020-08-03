from bs4 import BeautifulSoup
import requests

res=requests.get('https://en.wikipedia.org/wiki/Web_scraping')

soup=BeautifulSoup(res.text,'lxml')

for link in soup.find_all('a',href=True):#requesting a tags with attribute href
    print(link['href'])#asking only href else all attributes with tags will b displayed
    