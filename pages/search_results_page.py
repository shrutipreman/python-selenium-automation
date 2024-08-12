from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//h2[@data-test='resultsHeadingWithoutCount']")
   # ADD_TO_CART_BTN = (By.CSS_SELECTOR,"button[id*='addToCartButton']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_CART_BTN= (By.CSS_SELECTOR, "button.sc-9306beff-0.sc-acb41a74-0.dfqbQr.dbtwRO")

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'chocolate' in actual_text, f'Expected chocolate not in actual {actual_text}'
        sleep(6)

    def verify_url(self):
        url = self.driver.current_url
        assert 'chocolate' in url, f'Expected "chocolate" not in {url}'

    def add_product_cart(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
        sleep(3)
        self.click(*self.ADD_TO_CART_BTN)
    def add_side_nav(self):
        self.click(*self.SIDE_CART_BTN)