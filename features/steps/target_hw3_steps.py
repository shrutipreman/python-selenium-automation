from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open target main page')
def open_target(context):
    context.app.main_page.open()


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()
    #context.driver.find_element(By.CSS_SELECTOR, ".sc-e9170b4b-2.loaHYA").click()
    sleep(2)

@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    context.app.cart_page.verify_cart_empty()

    #expected_result = 'Your cart is empty'
    #actual_result = context.driver.find_element(By.CSS_SELECTOR,"h1.sc-fe064f5c-0.dtCtuk").text
    #assert expected_result in actual_result, f'Expected text did not match'
    #print('Test case passed')


@when('Click Sign In')
def click_signin(context):
    context.app.header.click_signin()
    #context.driver.find_element(By.CSS_SELECTOR,".sc-ab4ee1d1-1.sc-58ad44c0-1.bYXfno.libdhi" ).click()
    sleep(2)
@when ('right side navigation menu, click Sign In')
def click_sidenav_signin(context):
    context.app.header.click_sidenav_signin()
    #context.driver.find_element(By.XPATH,"//span[text()='Sign in' and @class='sc-859e7637-0 hHZPQy']").click()
    sleep(2)

@then('Verify Sign In form opened')
def verify_signin_form(context):
    context.app.login_page.verify_signin_form()
    #expected_result = 'Sign into your Target account'
    #actual_result = context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
    #assert expected_result in actual_result, f'Signin form did not open as expected'
    #print('Test case passed')
