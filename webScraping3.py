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




