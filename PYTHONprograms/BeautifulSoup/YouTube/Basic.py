from bs4 import BeautifulSoup
import requests
import lxml

res=requests.get('https://coreyms.com/')#returns an object of  requests
#print(res.text)
soup=BeautifulSoup(res.text,'lxml')#conversts requests object to bs4 object

title=soup.select('title')
#to select the html tags Syntax-object.select('Html tags')
# the title consists of all the information within the the title tags
# in the form of list
print(title[0].text)# getText method is used get only the text without the tags

