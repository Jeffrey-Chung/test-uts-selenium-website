'''
This script will run the tests on chrome
'''
import unittest
from selenium import webdriver
import utilities

class UItestChrome(unittest.TestCase):
    '''
    Class to run tests on Google Chrome
    '''
    def test_uts_website(self):
        '''
        Test to check if test has been ran successfully
        '''
        self.assertEqual(utilities.ui_test(chrome_driver), "Test has ran sucessfully")

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    utilities.set_options(chrome_options)
    # Configure the driver
    chrome_driver = utilities.setup_driver(chrome_options)
    unittest.main()
