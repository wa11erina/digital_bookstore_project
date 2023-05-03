import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.class_base import Base

class Personal_info(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators


    about_me = "//a[@class='user_menu__about_me']"
    edit_name = "//*[@id='personal-about']/li[2]/div[1]/span"
    first_name = "//*[@id='personal-about']/li[2]/div[2]/form/input[1]"
    last_name = "//*[@id='personal-about']/li[2]/div[2]/form/input[2]"
    ok_button = "//*[@id='personal-about']/li[2]/div[2]/form/button"
    words_about_me_edit = "//*[@id='personal-about']/li[5]/div/span"
    words_about_me = "//*[@id='personal-about']/li[5]/form/div[1]/textarea"
    save_button = "//*[@id='personal-about']/li[5]/form/button[1]"



    # Getters


    def get_about_me(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_me)))

    def get_edit_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.edit_name)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_ok_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ok_button)))

    def get_words_about_me_edit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.words_about_me_edit)))

    def get_words_about_me(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.words_about_me)))

    def get_save_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_button)))



    # Actions


    def click_about_me(self):
        self.get_about_me().click()
        print("Navigate to About Me section")

    def click_edit_name(self):
        self.get_edit_name().click()
        print("Edit name icon pushed")

    def clear_first_name(self):
        self.get_first_name().clear()
        print("First name field is empty")

    def input_first_name(self, name):
        self.get_first_name().send_keys(name)
        print("First name input")

    def clear_last_name(self):
        self.get_last_name().clear()
        print("Last name field is empty")

    def input_last_name(self, name):
        self.get_last_name().send_keys(name)
        print("Last name input")

    def click_ok_button(self):
        self.get_ok_button().click()
        print("Ok button pushed")

    def click_words_about_me_edit(self):
        self.get_words_about_me_edit().click()
        print("Edit words about me")

    def clear_words_about_me(self):
        self.get_words_about_me().clear()
        print("About Me field is empty")

    def input_words_about_me(self, words):
        self.get_words_about_me().send_keys(words)
        print("Words about me input")

    def click_save_button(self):
        self.get_save_button().click()
        print("Save button pushed")



    # Methods


    def input_personal_info(self):
        self.get_current_url()
        self.click_about_me()
        self.click_edit_name()
        self.clear_first_name()
        self.input_first_name("QA")
        self.clear_last_name()
        self.input_last_name("Student")
        self.click_ok_button()
        self.click_words_about_me_edit()
        self.clear_words_about_me()
        self.input_words_about_me("Think different")
        self.click_save_button()
        self.assert_url("https://www.litres.ru/pages/personal_cabinet_about_me/")
        time.sleep(5)
        self.make_screenshot()
