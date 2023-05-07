import time
import allure

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.class_base import Base


class Book_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Getting book info from the book page and adding book to Cart"""

    # Locators


    book_title = "//*[@id='page-wrap']/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/h1"
    book_price = "//*[@id='reg_buynow']/form/button/span[2]"
    exception = "//button[@class='biblio_book_drm__button btn btn-orange coolbtn']"
    book_cart_icon = "//button[@data-action='addbasket']"
    discount_pop_up_close = "//*[@id='promo-books-popup']/a"
    cart_icon = "//button[@data-action='dropbasket']"


    # Getters


    def get_book_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_title)))

    def get_book_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_price)))

    def get_exception(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exception)))

    def get_book_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_cart_icon)))

    def get_discount_pop_up_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discount_pop_up_close)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon)))


    # Actions


    def print_book_title(self):
        value_book_title = self.get_book_title().text
        print(value_book_title)

    def print_book_price(self):
        try:
            value_book_price = self.get_book_price().text
            print(value_book_price)
        except TimeoutException:
            value_exception = self.get_exception().text
            exception_price = value_exception.replace("ПЕРЕЙТИ К ПОКУПКЕ ЗА ", "")
            print(exception_price)

    def add_book_to_cart(self):
        self.get_book_cart_icon().click()
        print("The book added to Cart")

    def close_discount_pop_up(self):
        self.get_discount_pop_up_close().click()
        print("Pop up closed")

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Navigate to Cart")



    # Methods


    def book_info(self):

        with allure.step("Book info"):

            """Get current URL"""
            self.get_current_url()

            """Print book title from book page"""
            self.print_book_title()

            """Print final book price with discount from book page"""
            self.print_book_price()

            """Click button with cart icon"""
            self.add_book_to_cart()

            """Close the pop-up about discounts"""
            self.close_discount_pop_up()

            """Wait so not to click the wrong button"""
            time.sleep(3)

            """Click cart icon one more time so to go to Cart"""
            self.click_cart_icon()

