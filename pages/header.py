from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, ".sc-e9170b4b-2.loaHYA")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGNIN_BTN = (By.CSS_SELECTOR,".sc-ab4ee1d1-1.sc-58ad44c0-1.bYXfno.libdhi" )
    SIDE_SIGNIN_BTN = (By.XPATH,"//span[text()='Sign in' and @class='sc-859e7637-0 hHZPQy']")
    def search_product(self):
        self.input_text('chocolate', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)
    def click_cart(self):
        self.click(*self.CART_BTN)

    def click_signin(self):
        self.click(*self.SIGNIN_BTN)

    def click_sidenav_signin(self):
        self.click(*self.SIDE_SIGNIN_BTN)


