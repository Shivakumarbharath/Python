from bs4 import BeautifulSoup
import requests

res=requests.get('https://en.wikipedia.org/wiki/Web_scraping')

soup=BeautifulSoup(res.text,'lxml')

#selecting the class
#soup.select('.class_name')

subheadings=soup.select('.toctext')
# this object contains information with tags
# to print it without tags we use for loop

for i in subheadings:
    print(i.getText())
