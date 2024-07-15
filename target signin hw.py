from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# clicks on the signin button
driver.find_element(By.XPATH,"//span[text()='Sign in']").click()
sleep(5)
# Click SignIn from side navigation
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn'] //span[text()='Sign in']").click()
sleep(5)

# Verify SignIn page opened:

# “Sign into your Target account” text is shown
expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
assert expected_result in actual_result
print('Test case passed')

#SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)

driver.find_element(By.XPATH,"//span[text()='Sign in with password']")
print('Signin button present')

sleep(10)