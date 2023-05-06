from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time

from pages.login_page import Login_page
from pages.personal_info_page import Personal_info


def test_personal_info(set_up):

    """Authorization, receiving confirmation of authorization and editing personal info"""

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

    """Editing personal info"""
    pi = Personal_info(driver)
    pi.input_personal_info()

    time.sleep(3)

    driver.close()
