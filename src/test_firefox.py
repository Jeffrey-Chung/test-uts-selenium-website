'''
This script will run the tests on firefox
'''
import unittest
from selenium import webdriver
import utilities

class UITestFirefox(unittest.TestCase):
    '''
    Class to run tests on Firefox
    '''
    def test_uts_website(self):
        '''
        Test to check if test has been ran successfully
        '''
        self.assertEqual(utilities.ui_test(firefox_driver), "Test has ran sucessfully")

if __name__ == "__main__":
    firefox_options = webdriver.FirefoxOptions()
    utilities.set_options(firefox_options)
    # Configure the driver
    firefox_driver = utilities.setup_driver(firefox_options)
    unittest.main()
