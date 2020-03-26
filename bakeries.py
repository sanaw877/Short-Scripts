import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd
import re

os.chdir(r'/Users/sundaswiqas/Downloads')
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

bakeries = pd.read_csv("Bakeries_in_NYC.csv")
bakeries['DBA'] = bakeries['DBA'].str.lower()
drop_kws = 'cookie|cake|cupcake|cafe|patisserie|confection|pastry|sweet|ritz carlton'
bakeries = bakeries[~bakeries['DBA'].str.contains(drop_kws,regex=True)]


browser = webdriver.Chrome('/Users/sundaswiqas/Desktop/chromedriver')
browser.get('http://www.google.com')
search_box = browser.find_element_by_name('q')
search_box.send_keys('maison kayser')
search_box.submit()


# for bakery in bakeries['DBA']:
# 	search_box.send_keys(bakery)
# 	search_box.submit()

results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')
results[0].click()
for a in browser.find_elements_by_tag_name('a'):
	print(a.text)

browser.quit()
# txt = browser.find_elements_by_tag_name('p')

# for elem in txt:
# 	print(elem.text)
# browser.quit()
