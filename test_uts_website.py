from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import random
import unittest


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

#firefox_service = Service('/usr/local/bin/geckodriver')
firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_argument("--ignore-certificate-errors")
firefox_options.add_argument("--private")
firefox_options.add_argument("--headless")
firefox_options.add_argument("--width=1920")
firefox_options.add_argument("--height=1080")
#firefox_driver = webdriver.Firefox(service = firefox_service, options = firefox_options)

firefox_driver = webdriver.Remote(
command_executor='http://localhost:4444',
options=firefox_options)
firefox_driver.get('https://www.uts.edu.au/')


def ui_test(driver):
        try:  
        #Check if the website has a valid certificate by starting with http://
            if driver.current_url.startswith('https://'):
                print("The website has a valid certificate.")
            else:
                print("The website does not have a valid certificate.")

            
            #Click on Arrow keys on What's Happening Section
            left_arrow_key = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/button[1]').click()
            right_arrow_key = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/button[2]').click()
            
            random_course_index = random.randint(1, 13)
            print("You have tested this course area: " + undergrad_and_postgrad_course_areas[random_course_index-1])
            #Click on Explore Course Areas -> Finds a random course area to choose from
            explore_course_areas_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/section/h4').click()
            undergrad_and_postgrad_course_areas_button = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/section/div/ul/li[{random_course_index}]/a').click()

            #Click on Study Button -> Randomly finds a course to choose from to test
            study_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[4]/nav/ul/li[1]/span').click()
            find_a_course_button = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/main/ul/li[1]/nav/div/ul/li[{random_course_index}]/a').click()

            #Click on Search Button then close Search Bar
            search_button = driver.find_element("id", 'site-search-toggle').click()
            search_text = driver.find_element("id", 'edit-search-keys').send_keys("UTS")
            close_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div[2]/button').click()
            

            #Click on Staff Button, only the search button test and staff button test can work one at a time
            staff_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/nav/ul/li[1]/a').click()   
        
        finally:
            driver.quit()
            successful_run = "Test has ran sucessfully"
            return successful_run
            

class UITest(unittest.TestCase):
    def test_uts_website(self):
         self.assertEqual(ui_test(firefox_driver), "Test has ran sucessfully")

    
if __name__ == "__main__":
    unittest.main()
