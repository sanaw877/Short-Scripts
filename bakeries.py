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


for bakery in bakeries[3:5]:
	browser.get('http://www.google.com')
	search_box = browser.find_element_by_name('q')
	search_box.send_keys(bakery)
	search_box.submit()

	try:
	# results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')
		links = browser.find_elements_by_css_selector('div.r > a')
		first_result = links[0].get_attribute("href")

		time.sleep(5)

		headers = {'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
		session = requests.Session()
		page = session.get(first_result, headers=headers)
	except:
		pass
	
	if page.status_code == 200:

		soup = BeautifulSoup(page.content, 'html.parser')
		# print(soup.prettify())

		hrefs = []
		for link in soup.find_all('a'):
				href = link.get('href')
				if href:
					hrefs.append(href)
		
		if hrefs:		
			for href in hrefs:
				if 'menu' in href:
					href = soup.find_element_by_link_text()

	time.sleep(10)
	
browser.quit()
