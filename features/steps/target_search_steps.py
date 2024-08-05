from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()
    #context.driver.find_element(By.ID, 'search').send_keys(product)
    #context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #sleep(5)

@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_text()

    #actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    #assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    context.app.search_results_page.verify_url()

    #url = context.driver.current_url
    #assert expected_product in url, f'Expected {expected_product} not in {url}'