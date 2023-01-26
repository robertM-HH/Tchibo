from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class ProductPage():
    """
    This class defines the functions for interacting with the ProductPage of a website using
    Selenium webdriver.

    The class provides the following methods:

        * assert_searched_product(): It asserts that the searched product is present on the 
          product page by checking the visibility of the product title.
    
    It uses the WebDriverWait class to ensure that elements are present before interacting with
    them and the expected_conditions module to define the conditions for the elements to be present.
    The class also imports a Locators module that contains the locators of the elements in the page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.yogamatte_tittle_xpath = Locators.yogamatte_tittle_xpath

    def assert_searched_product(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.yogamatte_tittle_xpath)))