import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.class_base import Base


class Final_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    my_books_menu = "//a[@href='/pages/my_books_all/']"
    my_books_cart = "//a[@href='/pages/new_basket/']"
    remove_book = "//*[@id='__next']/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/button[2]"
    want_to_remove = "//*[@id='modal']/div[1]/div/div/div/div[3]/div[1]/button/div"


    # Getters


    def get_my_books_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_books_menu)))

    def get_my_books_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_books_cart)))

    def get_remove_book(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_book)))

    def get_want_to_remove(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.want_to_remove)))



    # Actions


    def navigate_back(self):
        self.driver.back()
        print("Navigate back")

    def click_my_books_menu(self):
        self.get_my_books_menu().click()
        print("Navigate to My Books menu")

    def click_my_books_cart(self):
        self.get_my_books_cart().click()
        print("Navigate to the Cart")

    def click_remove_book(self):
        self.get_remove_book().click()
        print("Remove button pushed")

    def click_want_to_remove(self):
        self.get_want_to_remove().click()
        print("The book removed")



        # Methods


    def remove_book_from_cart(self):
        self.navigate_back()
        self.click_my_books_menu()
        self.click_my_books_cart()
        time.sleep(5)
        self.assert_url("https://www.litres.ru/pages/new_basket/")
        self.click_remove_book()
        time.sleep(5)
        self.click_want_to_remove()
