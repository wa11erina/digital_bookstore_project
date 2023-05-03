import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login_page
from pages.find_book_page import Find_book
from pages.book_page import Book_page
from pages.cart_page import Cart_page
from pages.payment_page import Payment_page
from pages.final_page import Final_page



@pytest.mark.run(order=1)
def test_buy_book_1(set_group, set_up):

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_page(driver)
    login.authorization()

    time.sleep(5)

    fb = Find_book(driver)
    fb.find_book_1()

    time.sleep(5)

    bp = Book_page(driver)
    bp.book_info()

    time.sleep(5)

    cp = Cart_page(driver)
    cp.assert_book_info_1()

    time.sleep(5)

    pp = Payment_page(driver)
    pp.payment()

    time.sleep(5)

    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(5)

    driver.close()


@pytest.mark.run(order=2)
def test_buy_book_2(set_up):

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_page(driver)
    login.authorization()

    time.sleep(5)

    fb = Find_book(driver)
    fb.find_book_2()

    time.sleep(5)

    bp = Book_page(driver)
    bp.book_info()

    time.sleep(5)

    cp = Cart_page(driver)
    cp.assert_book_info_2()

    time.sleep(5)

    pp = Payment_page(driver)
    pp.payment()

    time.sleep(5)

    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(5)

    driver.close()


@pytest.mark.run(order=4)
def test_buy_book_3(set_up):

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_page(driver)
    login.authorization()

    time.sleep(5)

    fb = Find_book(driver)
    fb.find_book_3()

    time.sleep(5)

    bp = Book_page(driver)
    bp.book_info()

    time.sleep(5)

    cp = Cart_page(driver)
    cp.assert_book_info_3()

    time.sleep(5)

    pp = Payment_page(driver)
    pp.payment()

    time.sleep(5)

    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(5)

    driver.close()


@pytest.mark.run(order=3)
def test_buy_book_4(set_up):

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_page(driver)
    login.authorization()

    time.sleep(5)

    fb = Find_book(driver)
    fb.find_book_4()

    time.sleep(5)

    bp = Book_page(driver)
    bp.book_info()

    time.sleep(5)

    cp = Cart_page(driver)
    cp.assert_book_info_4()

    time.sleep(5)

    pp = Payment_page(driver)
    pp.payment()

    time.sleep(5)

    fp = Final_page(driver)
    fp.remove_book_from_cart()

    time.sleep(5)

    driver.close()

