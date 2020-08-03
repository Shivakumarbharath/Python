import urllib.request

url="https://www.python.org/static/img/python-logo.png"


urllib.request.urlretrieve(url,"python.jpeg")#to download image syntax- urllib.request.urlretrieve(url,'filename')