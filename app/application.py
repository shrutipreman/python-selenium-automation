from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.base_page import Page
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.login_page = LoginPage(driver)

