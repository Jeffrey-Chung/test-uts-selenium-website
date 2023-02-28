from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()
firefox_service = Service('/usr/local/bin/geckodriver')
firefox_options = Options()
#firefox_options.add_argument("--ignore-certificate-errors")
firefox_options.add_argument("--private")
#firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920,1080")
#driver = webdriver.Chrome(service=s, options=options)
driver = webdriver.Firefox(service = firefox_service, options = firefox_options)
driver.get('https://www.uts.edu.au/')
driver.open()
'''
try:

finally:
    driver.quit()
    '''