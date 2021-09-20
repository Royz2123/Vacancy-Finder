import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import constants

options = Options()
options.binary_location = r"C://Program Files//Mozilla Firefox//firefox.exe"
driver = webdriver.Firefox(options=options)

driver.get('http://www.google.co.il/')
driver.find_element_by_link_text('חיפוש תמונות').click()

time.sleep(10)

driver.close()