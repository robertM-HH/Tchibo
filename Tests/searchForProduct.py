import unittest
import HtmlTestRunner
import chromedriver_binary # Adds chromedriver binary to path
from selenium import webdriver
from Pages.homePage import HomePage
from Pages.productPage import ProductPage

class SearchForProductTest(unittest.TestCase):
    """
    This script uses the unittest module to create a test case for searching for a product
    on the Tchibo website. The test case uses the Selenium webdriver to open the Tchibo website,
    interact with elements on the website using the HomePage and ProductPage classes,
    and asserts that the correct product is displayed on the product page.
    The test case uses the HtmlTestRunner to generate a report of the test execution.
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        
    def test_search_for_product(self):
        driver = self.driver
        driver.get("https://www.tchibo.de/")
        homepage = HomePage(driver)
        productpage = ProductPage(driver)
        homepage.click_accept_datenschutz()
        homepage.search_for_product("komfort-Yogamatte")
        homepage.search_select_first_option()
        productpage.assert_searched_product()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Work/Python/virtual env/Tchibo/task1/task1_venv/reports'))