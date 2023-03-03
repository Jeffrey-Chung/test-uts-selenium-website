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
#driver.open()

try:
    #Check if the website has a valid certificate by starting with http://
    if driver.current_url.startswith('https://'):
        print("The website has a valid certificate.")
    else:
        print("The website does not have a valid certificate.")

    #Click on Search Button then close Search Bar
    search_button = driver.find_element(By.XPATH, '//*[@id="site-search-toggle"]').click()
    search_text = driver.find_element(By.XPATH, '//*[@id="edit-search-keys"]').send_keys("UTS")
    close_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div[2]/button').click()

    #Click on Arrow keys on What's Happening Section
    left_arrow_key = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/button[1]').click()
    right_arrow_key = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/button[2]').click()
    
    #Click on Explore Course Areas -> Analytics and Data Science
    explore_course_areas_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/section/h4').click()
    analytics_and_data_science_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/section/div/ul/li[1]/a').click()

    #Click on Study Button -> Information Technology
    study_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[4]/nav/ul/li[1]/span').click()
    information_technology_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/ul/li[1]/nav/div/ul/li[9]/a').click()

    #Click on Staff Button, only the search button test and staff button test can work one at a time
    staff_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/nav/ul/li[1]/a').click()

   
finally:
    driver.quit()
    