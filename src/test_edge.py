'''
This script will run the tests on edge
'''
import unittest
from selenium import webdriver
import utilities

class UITestEdge(unittest.TestCase):
    '''
    Class to run tests on Microsoft Edge
    '''
    def test_uts_website(self):
        '''
        Test to check if test has been ran successfully
        '''
        self.assertEqual(utilities.ui_test(edge_driver), "Test has ran sucessfully")

if __name__ == "__main__":
    edge_options = webdriver.EdgeOptions()
    utilities.set_options(edge_options)
    # Configure the driver
    edge_driver = utilities.setup_driver(edge_options)
    unittest.main()
