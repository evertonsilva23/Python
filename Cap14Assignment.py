import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

print('Retrieving:', url)

def getlink(p):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    i = 0
    tags = soup('a')
    for tag in tags:
        if i == p-1:
            link = tag.get('href', None)

        i += 1
    return(link)
c = 0
while c < count:
    url = getlink(pos)
    print('Retrieving:', url)
    c += 1
    