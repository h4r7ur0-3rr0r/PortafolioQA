from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage
import time

class SearchPage(BasePage):
    #NEW_CONDITION_FILTER = (By.XPATH, "//span[contains(text(), 'Nuevo')]")
    NEW_CONDITION_FILTER = (By.XPATH, '//span[@class="ui-search-filter-name" and text()="Nuevo"]')
    SORT_DROPDOWN = (By.CLASS_NAME, "andes-dropdown__trigger")
    HIGHER_PRICE_OPTION = (By.XPATH, "//span[contains(text(), 'Mayor precio')]")
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, ".poly-card--mobile")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".poly-card--mobile .poly-component__title")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".andes-money-amount")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def filter_by_new_condition(self):
        self.take_screenshot("05_before_new_filter")
        self.driver.execute_script("window.scrollTo(0, 450);")
        self.click_element(self.NEW_CONDITION_FILTER)
        self.take_screenshot("06_after_new_filter")
        time.sleep(5)
    
    def sort_by_higher_price(self):
        self.take_screenshot("09_before_sorting")
        time.sleep(3)
        self.click_element(self.SORT_DROPDOWN)
        self.click_element(self.HIGHER_PRICE_OPTION)
        self.take_screenshot("10_after_sorting")
        time.sleep(5)

    def get_top_products(self, quantity=5):
        containers = self.driver.find_elements(*self.PRODUCT_CONTAINER)[:quantity]
        names = self.get_elements_texts(self.PRODUCT_NAMES)[:quantity]
        prices = self.get_elements_texts(self.PRODUCT_PRICES)[:quantity]
        
        products = []
        for container in containers:
            name = container.find_element(*self.PRODUCT_NAMES).text
            price = container.find_element(*self.PRODUCT_PRICES).text
            products.append({
                    "name": name.strip(),
                    "price": f"${price.strip()}"
                    
            })
            print(products)      
        self.take_screenshot("11_results")
        return products