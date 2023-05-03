from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.class_base import Base


class Cart_page(Base):

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
        self.get_current_url()
        self.print_book_title_cart()
        self.assert_book_title(self.get_book_title_cart(), "Стив Джобс")
        self.print_book_price_cart()
        self.assert_book_price(self.get_book_price_cart(), "399,00 ₽")
        self.make_screenshot()

    def assert_book_info_2(self):
        self.get_current_url()
        self.print_book_title_cart()
        self.assert_book_title(self.get_book_title_cart(), "Managing the Testing Process. Practical Tools and Techniques for Managing Hardware and Software Testing")
        self.print_book_price_cart()
        self.assert_book_price(self.get_book_price_cart(), "4 267,89 ₽")
        self.make_screenshot()

    def assert_book_info_3(self):
        self.get_current_url()
        self.print_book_title_cart()
        self.assert_book_title(self.get_book_title_cart(), "Что такое тестирование. Курс молодого бойца")
        self.print_book_price_cart()
        self.assert_book_price(self.get_book_price_cart(), "499,00 ₽")
        self.make_screenshot()

    def assert_book_info_4(self):
        self.get_current_url()
        self.print_book_title_cart()
        self.assert_book_title(self.get_book_title_cart(), "Ловушка для багов. Полевое руководство по веб-хакингу (pdf + epub)")
        self.print_book_price_cart()
        self.assert_book_price(self.get_book_price_cart(), "649,00 ₽")
        self.make_screenshot()

