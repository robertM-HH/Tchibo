import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class HomePage():
    """
    This class defines the functions for interacting with the HomePage of a website using 
    Selenium webdriver.
    
    The class provides the following methods:
    
        * click_accept_datenschutz(): It clicks on the accept button on the data privacy policy 
          pop-up.
        * search_for_product(productName: str): It enters the productName in the search input 
          field and clears the field first.
        * search_select_first_option(): It clicks on the first option from the search results.
        
    It also uses the WebDriverWait class to ensure that elements are present before interacting with
    them and the expected_conditions module to define the conditions for the elements to be present.
    The class also imports a Locators module that contains the locators of the elements in the page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.datenschutz_popup_accept_id = Locators.datenschutz_popup_accept_id
        self.search_input_field_xpath = Locators.search_input_field_xpath
        self.search_result_first_option_css = Locators.search_result_first_option_css
     
    def click_accept_datenschutz(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.datenschutz_popup_accept_id))).click()
         
    def search_for_product(self, productName):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search_input_field_xpath))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search_input_field_xpath))).send_keys(productName)
        
    def search_select_first_option(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.search_result_first_option_css))).click()