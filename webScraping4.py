# Melon Daily Chart Top 50
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/day/index.htm"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

driver.get(url)
bsObject = BeautifulSoup(driver.page_source, "html.parser")

# Extract the title of songs
title_songs = []
for song in bsObject.find_all('tr', {'class':'lst50'}):
    title = song.select('input')[0].get('title')
    title_songs.append(title)

for song in title_songs:
    print(song)
