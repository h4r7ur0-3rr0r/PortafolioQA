from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage
import time

class HomePage(BasePage):
    COUNTRY_SELECTOR = (By.ID, "MX")
    SEARCH_BAR = (By.NAME,  "as_word")
    SEARCH_BUTTON = (By.CLASS_NAME, "nav-search-btn")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def select_country(self):
        self.take_screenshot("01_before_country_selection")
        self.click_element(self.COUNTRY_SELECTOR)
        self.take_screenshot("02_after_country_selection")
        time.sleep(3)
    
    def search_for(self,text):
        self.take_screenshot("03_before_search")
        self.send_keys(self.SEARCH_BAR, text)
        self.click_element(self.SEARCH_BUTTON)
        self.take_screenshot("04_after_search")
        time.sleep(3)