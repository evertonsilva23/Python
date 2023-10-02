from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


# Retrieve all of the tags span
tags = soup('span')
counts = 0

for tag in tags:
    number = int(tag.contents[0])
    counts = counts + number
print(counts)
