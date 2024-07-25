from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@then('Verify there are 10 benefit cells')
def verify_cell_number(context):
    cells = context.driver.find_elements(By.CSS_SELECTOR,".sc-fb3945a7-5.fBbzFg")
    assert len(cells) == 10, f'Expected 10 benefit cells but only {len(cells)}'
    print(f"there are {len(cells)} benefit cells")