# Web scraping: Kyobobook - Bestsellers

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Open the Kyobobook Bestseller web page
html = urlopen('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf')
bsObject = BeautifulSoup(html, "html.parser")

# Extract the url for each book
book_page_urls = []
for cover in bsObject.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page_urls.append(link)

# Extract essential data from metadata
for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html, "html.parser")
    title = bsObject.find('meta', {'property':'eg:itemName'}).get('content')
    author = bsObject.select('span.name a')[0].text
    image = bsObject.find('meta', {'property':'eg:itemImage'}).get('content')
    url = bsObject.find('meta', {'property':'eg:itemUrl'}).get('content')
    originalPrice = bsObject.find('meta', {'property':'eg:originalPrice'}).get('content')
    salePrice = bsObject.find('meta', {'property':'eg:salePrice'}).get('content')

    print(index+1, title, author, image, url, originalPrice, salePrice)
