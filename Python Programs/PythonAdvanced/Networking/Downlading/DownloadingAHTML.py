'''
To download a conents of url using urllib
on to local machine
'''

import urllib.error
import urllib.request

try:

    url=urllib.request.urlopen("https://www.python.org/")#the method that takes the url

    content=url.read()

    url.close()
    f = open("python.html", "wb")
    f.write(content)  # it contains complete html page without style
    f.close()

except urllib.error.HTTPError:
    print("URL not found")

