import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd
import re
from bs4 import BeautifulSoup
import requests
import cv2
import pytesseract
import shutil
from skimage import io


os.chdir(r'/Users/sundaswiqas/Downloads')
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

bakeries = pd.read_csv("Bakeries_in_NYC.csv")
bakeries['DBA'] = bakeries['DBA'].str.lower()
drop_kws = 'cookie|cake|cupcake|cafe|patisserie|confection|pastry|sweet|ritz carlton|cinnabon'
bakeries = bakeries[~bakeries['DBA'].str.contains(drop_kws,regex=True)]
# bakeries.to_excel('bakeries_list.xlsx')

bakeries = bakeries['DBA'].to_list()

browser = webdriver.Chrome('/Users/sundaswiqas/Desktop/chromedriver')


for bakery in bakeries:
	browser.get('http://www.google.com')
	search_box = browser.find_element_by_name('q')
	search_box.send_keys(bakery)
	search_box.submit()

	try:
	# results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')
		links = browser.find_elements_by_css_selector('div.r > a')
		first_result = links[0].get_attribute("href")

		browser.get(first_result)
		time.sleep(5)
	except:
		print('Nothing found.')

	links = browser.find_elements_by_xpath('//a[@href]')
	menu_links = [link.get_attribute("href") for link in links if 'menu' in link.get_attribute("href")]
	print(menu_links)

	for href in menu_links:
		browser.get(href)
		content = browser.find_elements_by_css_selector('body')
		images = browser.find_elements_by_css_selector('img')
		
		print(href)
		print(content[0].text)

		for img in images:
			img = img.get_attribute('src')
			r = requests.get(img, stream=True, headers={'User-agent': 'Mozilla/5.0'})
			if r.status_code == 200:
				with open("img.png", 'wb') as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw,f)
			image = io.imread('img.png')
			text = pytesseract.image_to_string(image)
			print(text)
		

		time.sleep(5)
	
browser.quit()
