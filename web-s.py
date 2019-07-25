#!/usr/bin/env

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("http://www.google.com/xhtml")
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()


'''
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
'''
