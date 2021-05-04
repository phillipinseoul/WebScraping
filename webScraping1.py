# Web scraping: Naver

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

# print(bsObject)     # Print the whole HTML
# print(bsObject.head.title)      # Print title

# for meta in bsObject.head.find_all('meta'):   # Print all metadata
#     print(meta.get('content'))

for link in bsObject.find_all('a'):             # Print all href links
    print(link.text.strip(), link.get('href'))



