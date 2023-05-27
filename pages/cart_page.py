import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.class_base import Base
from logger import Logger


class Cart_page(Base):
    """Comparing book title and book price from the Cart page with the one from the Book page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators


    book_title_cart = "//a[@class='Cart-module__bookCard__link_2vZQZ']"
    book_price_cart = "//div[@class='CheckoutBox-module__costs__price_1HeDU CheckoutBox-module__costs__info_total_15QTT']"


    # Getters


    def get_book_title_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_title_cart)))

    def get_book_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_price_cart)))


    # Actions


    def print_book_title_cart(self):
        value_book_title_cart = self.get_book_title_cart().text
        print(value_book_title_cart)


    def print_book_price_cart(self):
        value_book_price_cart = self.get_book_price_cart().text
        print(value_book_price_cart)


    # Methods


    def assert_book_info_1(self):

        with allure.step("Assert book info 1"):

            Logger.add_start_step(method="assert_book_info_1")

            """Get current URL"""
            self.get_current_url()

            "Print book title from the Cart page"
            self.print_book_title_cart()

            """Compare book title from the Cart page with the one from the Book page"""
            self.assert_book_title(self.get_book_title_cart(), "Стив Джобс")

            "Print final book price with discounts from the Cart page"
            self.print_book_price_cart()

            """Compare book price from the Cart with the one from the Book page"""
            self.assert_book_price(self.get_book_price_cart(), "399,00 ₽")

            """Make screenshot of book in the Cart"""
            self.make_screenshot()

            Logger.add_end_step(url=self.driver.current_url, method="assert_book_info_1")


    def assert_book_info_2(self):

        with allure.step("Assert book info 2"):

            Logger.add_start_step(method="assert_book_info_2")

            """Get current URL"""
            self.get_current_url()

            "Print book title from the Cart page"
            self.print_book_title_cart()

            """Compare book title from the Cart page with the one from the Book page"""
            self.assert_book_title(self.get_book_title_cart(), "Managing the Testing Process. Practical Tools and Techniques for Managing Hardware and Software Testing")

            "Print final book price with discounts from the Cart page"
            self.print_book_price_cart()

            """Compare book price from the Cart with the one from the Book page"""
            self.assert_book_price(self.get_book_price_cart(), "4 268,21 ₽")

            """Make screenshot of book in the Cart"""
            self.make_screenshot()

            Logger.add_end_step(url=self.driver.current_url, method="assert_book_info_2")


    def assert_book_info_3(self):

        with allure.step("Assert book info 3"):

            Logger.add_start_step(method="assert_book_info_3")

            """Get current URL"""
            self.get_current_url()

            "Print book title from the Cart page"
            self.print_book_title_cart()

            """Compare book title from the Cart with the one from the Book page"""
            self.assert_book_title(self.get_book_title_cart(), "Что такое тестирование. Курс молодого бойца")

            "Print final book price with discounts from the Cart page"
            self.print_book_price_cart()

            """Compare book price from the Cart with the one from the Book page"""
            self.assert_book_price(self.get_book_price_cart(), "499,00 ₽")

            """Make screenshot of book in the Cart"""
            self.make_screenshot()

            Logger.add_end_step(url=self.driver.current_url, method="assert_book_info_3")


    def assert_book_info_4(self):

        with allure.step("Assert book info 4"):

            Logger.add_start_step(method="assert_book_info_4")

            """Get current URL"""
            self.get_current_url()

            "Print book title from the Cart page"
            self.print_book_title_cart()

            """Compare book title from the Cart page with the one from the Book page"""
            self.assert_book_title(self.get_book_title_cart(), "Ловушка для багов. Полевое руководство по веб-хакингу (pdf + epub)")

            "Print final book price with discounts from the Cart page"
            self.print_book_price_cart()

            """Compare book price from the Cart with the one from the Book page"""
            self.assert_book_price(self.get_book_price_cart(), "649,00 ₽")

            """Make screenshot of book in the Cart"""
            self.make_screenshot()

            Logger.add_end_step(url=self.driver.current_url, method="assert_book_info_4")

