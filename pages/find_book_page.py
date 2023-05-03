import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains

from base.class_base import Base


class Find_book(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    main_page = "//a[@class='Logo-module__wrapper']"
    search_field = "//input[@name='q']"
    find_button = "//button[@type='submit']"
    checkbox_text = "//label[@class='Checkbox__label_1xulf']"
    high_rating_1 = "//*[@id='__next']/div[1]/div[2]/div/div/div[3]/div[1]/div[5]/div[1]/div[2]"
    book_1 = "//a[@href='/book/uolter-ayzekson/stiv-dzhobs-2691335/']"
    book_2 = "//a[@href='/book/rex-black/managing-the-testing-process-practical-tools-and-techniques-for-28969885/']"
    book_3 = "//a[@href='/book/olga-nazina/chto-takoe-testirovanie-kurs-molodogo-boyca-68998117/']"
    catalogue = "//div[@data-id='catalog']"
    knowledge_and_skills = "//a[@href='/genre/znaniya-navyki-201623/']"
    pc_literature = "//a[@href='/genre/kompyuternaya-literatura-5024/']"
    information_security = "//a[@href='/genre/infobezopasnost-192079/']"
    high_rating_2 = "//*[@id='__next']/div[1]/div[2]/div/div[2]/div[1]/div[8]/div[1]/div[1]/div[2]"
    checkbox_russian = "//label[@for='languages-ru']"
    book_4 = "//a[@href='/book/yavorski-p/lovushka-dlya-bagov-polevoe-rukovodstvo-po-veb-hakingu-pdf-epub-64083682/']"


    # Getters


    def get_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_page)))

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_find_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.find_button)))

    def get_checkbox_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_text)))

    def get_high_rating_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.high_rating_1)))

    def get_book_1(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        return WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, self.book_1)))

    def get_book_2(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        return WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, self.book_2)))

    def get_book_3(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        return WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, self.book_3)))

    def get_catalogue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalogue)))

    def get_knowledge_and_skills(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.knowledge_and_skills)))

    def get_pc_literature(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pc_literature)))

    def get_information_security(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.information_security)))

    def get_high_rating_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.high_rating_2)))

    def get_checkbox_russian(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_russian)))

    def get_book_4(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        return WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, self.book_4)))



    # Actions


    def go_to_main_page(self):
        self.get_main_page().click()
        print("Navigate to the Main page")

    def input_request(self, request):
        self.get_search_field().send_keys(request)
        print("Request entered")

    def click_find_button(self):
        self.get_find_button().click()
        print("Find button pushed")

    def mark_checkbox_text(self):
        self.get_checkbox_text().click()
        print("Checkbox Text marked")

    def activate_high_rating_1(self):
        self.get_high_rating_1().click()
        print("High rating toggle activated")

    def click_book_1(self):
        self.get_book_1().click()
        print("Navigate to the found book page")

    def click_book_2(self):
        self.get_book_2().click()
        print("Navigate to the found book page")

    def scroll_to_book_3(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_book_3()).perform()
        print("Scroll to the book")

    def click_book_3(self):
        self.get_book_3().click()
        print("Navigate to the found book page")

    def click_catalogue(self):
        self.get_catalogue().click()
        print("Navigate to Catalogue")

    def scroll_to_knowledge_and_skills(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_knowledge_and_skills()).perform()
        print("Scroll to 'Knowledge and skills section'")

    def go_to_knowledge_and_skills(self):
        self.get_knowledge_and_skills().click()
        print("Navigate to 'Knowledge and skills' section")

    def scroll_to_pc_literature(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_pc_literature()).perform()
        print("Scroll to PC literature")

    def go_to_pc_literature(self):
        self.get_pc_literature().click()
        print("Navigate to PC literature")

    def scroll_to_information_security(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_information_security()).perform()
        print("Scroll to Information Security")

    def go_to_information_security(self):
        self.get_information_security().click()
        print("Navigate to Information Security subgenre")

    def scroll_to_checkbox_text(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_checkbox_text()).perform()
        print("Scroll to checkbox Text")

    def scroll_to_high_rating_2(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_high_rating_2()).perform()
        print("Scroll to high rating toggle")

    def activate_high_rating_2(self):
        self.get_high_rating_2().click()
        print("High rating toggle activated")

    def mark_checkbox_russian(self):
        self.get_checkbox_russian().click()
        print("Checkbox Russian marked")

    def scroll_to_book_4(self):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_book_4()).perform()
            print("Scroll to the book")
        except TimeoutException:
            self.driver.execute_script("window.scroll(0,5000)")
            print("Scrolling")

    def click_book_4(self):
        self.get_book_4().click()
        print("Navigate to the found book page")



    # Methods


    def find_book_1(self):
        self.go_to_main_page()
        self.input_request("стив джобс")
        self.click_find_button()
        self.mark_checkbox_text()
        time.sleep(5)
        self.activate_high_rating_1()
        time.sleep(5)
        self.driver.refresh()
        self.click_book_1()

    def find_book_2(self):
        self.go_to_main_page()
        self.input_request("rex black")
        self.click_find_button()
        self.mark_checkbox_text()
        time.sleep(5)
        self.driver.refresh()
        self.click_book_2()

    def find_book_3(self):
        self.go_to_main_page()
        self.input_request("тестирование")
        self.click_find_button()
        self.mark_checkbox_text()
        time.sleep(5)
        self.activate_high_rating_1()
        time.sleep(5)
        self.scroll_to_book_3()
        self.driver.refresh()
        self.click_book_3()

    def find_book_4(self):
        self.go_to_main_page()
        self.click_catalogue()
        self.scroll_to_knowledge_and_skills()
        time.sleep(5)
        self.go_to_knowledge_and_skills()
        self.scroll_to_pc_literature()
        time.sleep(5)
        self.go_to_pc_literature()
        self.scroll_to_information_security()
        time.sleep(5)
        self.go_to_information_security()
        self.scroll_to_checkbox_text()
        time.sleep(5)
        self.mark_checkbox_text()
        time.sleep(5)
        self.scroll_to_high_rating_2()
        time.sleep(5)
        self.activate_high_rating_2()
        time.sleep(5)
        self.mark_checkbox_russian()
        time.sleep(5)
        self.scroll_to_book_4()
        time.sleep(5)
        self.driver.refresh()
        self.click_book_4()
