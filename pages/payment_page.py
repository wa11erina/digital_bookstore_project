import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.class_base import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    navigate_to_payment = "//div[@class='ButtonV3-module__buttonContent_3AZ1N']"


    # Getters


    def get_navigate_to_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.navigate_to_payment)))


    # Actions


    def click_navigate_to_payment(self):
        self.get_navigate_to_payment().click()
        print("Navigate to Payment")


    # Methods


    def payment(self):
        self.get_current_url()
        self.click_navigate_to_payment()
        time.sleep(5)
        self.make_screenshot()
