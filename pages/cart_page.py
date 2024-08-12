from selenium.webdriver.common.by import By

from pages.base_page import Page
class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1.sc-fe064f5c-0.dtCtuk")
    ITEM_NUMBER = (By.XPATH,"//div[@class='sc-c8b6049-2 xOFEL']//div//span[text()='1 item']")
    def verify_cart_empty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_result in actual_result, f'Expected text did not match'
        print('Test case passed')

    def item_present(self):
        count = self.driver.find_element(*self.ITEM_NUMBER).text
        assert count == '1 item', f"Expected number of item not in cart,currently {count} items present in cart"