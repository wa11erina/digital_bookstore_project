import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver


    """Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")


    """Assert current email"""

    def assert_email(self, email, result):
        value_email = email.text
        assert value_email == result
        print("Same email")


    """Assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Same URL")


    """Make screenshot"""

    def make_screenshot(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\ASUS\\PycharmProjects\\digital_bookstore_project\\screen\\' + name_screenshot)


    """Assert Book title"""

    def assert_book_title(self, book_title, result):
        value_book_title = book_title.text
        assert value_book_title == result
        print("Same book")


    """Assert Book price"""

    def assert_book_price(self, book_price, result):
        value_book_price = book_price.text
        assert value_book_price == result
        print("Same price")
