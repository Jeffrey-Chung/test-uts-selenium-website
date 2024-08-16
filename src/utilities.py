'''
This script stores all the common functions between the 3 test files. 
Including setup the drivers and the tests itself
In theory, you don't need to change anything on this script except adding your link to the driver.
'''
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

undergrad_and_postgrad_course_areas = [
'Analytics and Data Science',
'Business',
'Communication',
'Design, Architecture and Building',
'Education',
'Engineering',
'Health',
'Health(GEM)',
'Information Technology',
'International Studies and Social Sciences',
'Law',
'Science and Mathematics',
'Transdisciplinary Innovation'
]

def set_options(driver_options):
    '''
    function to set the same options for each browser
    '''
    driver_options.add_argument("--private")
    driver_options.add_argument("--headless")

def setup_driver(driver_options):
    '''
    function to configure settings for each driver
    '''
    driver = webdriver.Remote(
    command_executor="http://localhost:4444",
    options=driver_options
    )

    # Make sure you paste your URL in the line below
    driver.get('https://www.uts.edu.au/')
    return driver


def ui_test(driver):
    '''
    Conduct UI test for UTS website
    '''
    try:
    # Check if the website has a valid certificate by starting with http://
        if driver.current_url.startswith('https://'):
            print("The website has a valid certificate.")
        else:
            print("The website does not have a valid certificate.")

        # Click on Arrow keys on What's Happening Section
        left_arrow_key_xpath = '/html/body/div[1]/div[2]/div[1]/div/button[1]'
        right_arrow_key_xpath = '/html/body/div[1]/div[2]/div[1]/div/button[3]'
        driver.find_element(By.XPATH, left_arrow_key_xpath).click()
        driver.find_element(By.XPATH, right_arrow_key_xpath).click()

        rand_index = random.randint(1, 13)
        undergrad_and_postgrad_course = undergrad_and_postgrad_course_areas[rand_index-1]
        print("You have tested this course area: " + undergrad_and_postgrad_course)

        # Click on Explore Course Areas -> Finds a random course area to choose from
        shortened_xpath = '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/section/'
        explore_course_areas_xpath = shortened_xpath + 'h4'
        ug_and_pg_course_areas_xpath = shortened_xpath + f'div/ul/li[{rand_index}]/a'
        driver.find_element(By.XPATH, explore_course_areas_xpath).click()
        driver.find_element(By.XPATH, ug_and_pg_course_areas_xpath).click()

        # Click on Study Button -> Randomly finds a course to choose from to test
        find_course_xpath = f'/html/body/div[1]/div[3]/main/ul/li[1]/nav/div/ul/li[{rand_index}]/a'
        driver.get('https://www.uts.edu.au/study')
        driver.find_element(By.XPATH, find_course_xpath).click()

        # Click on Search Button then close Search Bar
        driver.find_element("id", 'site-search-toggle').click()
        driver.find_element("id", 'edit-search-keys').send_keys("UTS")
        driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div[2]/button').click()

        # Click on Staff Button
        # only the search button test and staff button test can work one at a time
        driver.get('https://staff.uts.edu.au/Pages/home.aspx')

    finally:
        result = "Test has ran sucessfully"
        driver.quit()
    return result
