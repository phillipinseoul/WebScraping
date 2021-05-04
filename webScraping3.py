# https://webnautes.tistory.com/1239
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://book.naver.com/bestsell/bestseller_list.nhn"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

# Open Naver Book Bestseller page
driver.get(url)
bsObject = BeautifulSoup(driver.page_source, "html.parser")

# Get the url for each book
book_page_urls = []
for index in range(0, 25):
    dl_data = bsObject.find('dt', {'id':'book_title_'+str(index)})
    link = dl_data.select('a')[0].get('href')
    book_page_urls.append(link)

# Extract neccessary info from metadata
for index, book_page_url in enumerate(book_page_urls):
    driver.get(book_page_url)
    bsObject = BeautifulSoup(driver.page_source, 'html.parser')

    title = bsObject.find('meta', {'property':'og:title'}).get('content')
    author = bsObject.find('dt', text='저자').find_next_siblings('dd')[0].text.strip()
    image = bsObject.find('meta', {'property':'og:image'}).get('content')
    url = bsObject.find('meta', {'property':'og:url'}).get('content')

    dd = bsObject.find('dt', text='가격').find_next_siblings('dd')[0]
    salePrice = dd.select('div.lowest strong')[0].text
    originalPrice = dd.select('div.lowest span.price')[0].text

    print(index+1, title, author, image, url, originalPrice, salePrice)