from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//h2[@data-test='resultsHeadingWithoutCount']")

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'chocolate' in actual_text, f'Expected chocolate not in actual {actual_text}'
        sleep(6)

    def verify_url(self):
        url = self.driver.current_url
        assert 'chocolate' in url, f'Expected "chocolate" not in {url}'
