import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, StaleElementReferenceException

from base.class_base import Base

class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.litres.ru/"


    # Locators


    accept_rules_button = "//*[@id='__next']/div[3]/div/div/div/div"
    login_window = "//a[@href='/pages/login/']"
    by_email = "//*[@id='__next']/div[1]/header/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div[1]"
    email_field = "//input[@name='email']"
    continue_button = "//*[@id='__next']/div[1]/header/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[2]"
    password_field = "//input[@name='pwd']"
    login_button = "//div[@class='AuthorizationPopup-module__step__block_xqj72']"
    profile = "//div[@class='Profile-module__wrapper_1aXs2']"
    login_info = "//a[@href='/pages/personal_cabinet_login/']"
    current_email = "//div[@class='user_email']"


    # Getters


    def get_accept_rules_button(self):
        return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable((By.XPATH, self.accept_rules_button))))

    def get_login_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_window)))

    def get_by_email_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.by_email)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_profile_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile)))

    def get_login_info(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        return WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, self.login_info)))

    def get_current_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_email)))




    # Actions


    def accept_rules(self):
        self.get_accept_rules_button().click()
        print("Rules accepted")

    def click_login_window(self):
        self.get_login_window().click()
        print("Login button pushed")

    def click_by_email_button(self):
        self.get_by_email_button().click()
        print("By Email button pushed")

    def input_email(self, email):
        self.get_email_field().send_keys(email)
        print("Email input")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Continue button pushed")

    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print("Password entered")

    def click_login_button(self):
        self.get_login_button().click()
        print("Login button pushed")

    def click_profile_icon(self):
        self.get_profile_icon().click()
        print("Profile icon pushed")

    def click_login_info(self):
        self.get_login_info().click()
        print("Navigate to Login Information section")



    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.accept_rules()
        self.click_login_window()
        self.click_by_email_button()
        self.input_email("qastudent2023@gmail.com")
        self.click_continue_button()
        self.input_password("StaleElementReferenceException")
        self.click_login_button()
        time.sleep(5)
        self.click_profile_icon()
        time.sleep(5)
        self.driver.refresh()
        self.click_login_info()
        self.assert_email(self.get_current_email(), "qastudent2023@gmail.com")



