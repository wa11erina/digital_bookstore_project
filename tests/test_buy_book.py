from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
import pytest
import allure

from pages.login_page import Login_page
from pages.find_book_page import Find_book
from pages.book_page import Book_page
from pages.cart_page import Cart_page
from pages.payment_page import Payment_page
from pages.final_page import Final_page


allure.description("Test buy book 1")
@pytest.mark.run(order=1)
def test_buy_book_1(set_group, set_up):

    """Smoke test: authorization, authorization confirmation, finding book in search using book title request, adding book to Cart, making the payment"""

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    """Authorization and receiving confirmation of authorization"""
    login = Login_page(driver)
    login.authorization()

    """Finding book in search using book title request"""
    fb = Find_book(driver)
    fb.find_book_1()

    """Getting book info from the book page and adding book to Cart"""
    bp = Book_page(driver)
    bp.book_info()

    """Comparing book title and book price from the Cart page with the one from the Book page"""
    cp = Cart_page(driver)
    cp.assert_book_info_1()

    """Payment"""
    pp = Payment_page(driver)
    pp.payment()

    time.sleep(3)

    """Removing book from Cart"""
    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(3)

    driver.close()


allure.description("Test buy book 2")
@pytest.mark.run(order=2)
def test_buy_book_2(set_up):

    """Smoke test: authorization, authorization confirmation, finding book in search using book author request, adding book to Cart, making the payment"""

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    """Authorization and receiving confirmation of authorization"""
    login = Login_page(driver)
    login.authorization()

    """Finding book in search using book author request"""
    fb = Find_book(driver)
    fb.find_book_2()

    """Getting book info from the book page and adding book to Cart"""
    bp = Book_page(driver)
    bp.book_info()

    """Comparing book title and book price from the Cart page with the one from the Book page"""
    cp = Cart_page(driver)
    cp.assert_book_info_2()

    """Payment"""
    pp = Payment_page(driver)
    pp.payment()

    time.sleep(3)

    """Removing book from Cart"""
    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(3)

    driver.close()


allure.description("Test buy book 3")
@pytest.mark.run(order=4)
def test_buy_book_3(set_up):

    """Smoke test: authorization, authorization confirmation, finding book in search using book theme request, adding book to Cart, making the payment"""

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    """Authorization and receiving confirmation of authorization"""
    login = Login_page(driver)
    login.authorization()

    """Finding book in search using book theme request"""
    fb = Find_book(driver)
    fb.find_book_3()

    """Getting book info from the book page and adding book to Cart"""
    bp = Book_page(driver)
    bp.book_info()

    """Comparing book title and book price from the Cart page with the one from the Book page"""
    cp = Cart_page(driver)
    cp.assert_book_info_3()

    """Payment"""
    pp = Payment_page(driver)
    pp.payment()

    time.sleep(3)

    """Removing book from Cart"""
    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(3)

    driver.close()


allure.description("Test buy book 4")
@pytest.mark.run(order=3)
def test_buy_book_4(set_up):

    """Critical path test: authorization, authorization confirmation, finding book in the catalogue, adding book to Cart, making the payment"""

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    """Authorization and receiving confirmation of authorization"""
    login = Login_page(driver)
    login.authorization()

    """Finding book in the catalogue"""
    fb = Find_book(driver)
    fb.find_book_4()

    """Getting book info from the book page and adding book to Cart"""
    bp = Book_page(driver)
    bp.book_info()

    """Comparing book title and book price from the Cart page with the one from the Book page"""
    cp = Cart_page(driver)
    cp.assert_book_info_4()

    """Payment"""
    pp = Payment_page(driver)
    pp.payment()

    time.sleep(3)

    """Removing book from Cart"""
    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(3)

    driver.close()

