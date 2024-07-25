from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep

@when('Add product to cart')
def add_product_cart(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,"[id*='addToCartButton']").click()
    sleep(5)
@when('Add to cart from side navigation')
def add_side_navg(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,".sc-9306beff-0.sc-d6c67707-0.dfqbQr.cfcjLp").click()
    sleep(3)

@when('Open cart page')
def open_cartpage(context):
    context.driver.get('https://www.target.com/cart')
    sleep(3)
@then('Verify  1 item is present in cart')
def verify_product(context):
    count = context.driver.find_element(By.XPATH,"//div[@class='sc-c8b6049-2 xOFEL']//div//span[text()='1 item']").text
    assert count == '1 item', f"Expected number of item not in cart,currently {count} items present in cart"













