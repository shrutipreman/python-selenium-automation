from selenium.webdriver.common.by import By

from pages.base_page import Page
class LoginPage(Page):
    LOGIN_PAGE_MSG= (By.XPATH, "//span[text()='Sign into your Target account']")
    def verify_signin_form(self):
        expected_result = 'Sign into your Target account'
        actual_result = self.driver.find_element(*self.LOGIN_PAGE_MSG).text
        assert expected_result in actual_result, f'Signin form did not open as expected'
        print('Test case passed')
