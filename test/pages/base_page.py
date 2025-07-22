from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def click_element(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
        except TimeoutException:
            print(f"element no disponible: {by_locator}")
            raise

    def send_keys(self, by_locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"element no visible para escribir: {by_locator}")
            raise

    def get_element_text(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located (by_locator)) 
            return element.text
        except TimeoutException:
            print(f"element no visible para obtener texto: {by_locator}")
            raise

    def get_elements_texts(self, by_locator):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
            return [element.text for element in elements]
        except TimeoutException:
            print(f"elements no encontrados: {by_locator}")
            return[]

    def take_screenshot(self, step_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path =  f"Report/screenshot_{step_name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path