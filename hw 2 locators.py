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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%3F&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# 1. locator for Amazon logo
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

# 2. locator for Email field
driver.find_element(By.ID,'ap_email')

# 3. locator for Continue button
driver.find_element(By.ID,'continue')

# 4. locator for Conditions of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

# 5.loactor for Privacy Notice link
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")

# 6. locator for Need help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")

# 7. locator for Forgot your password link
driver.find_element(By.ID,'auth-fpp-link-bottom')

# 8. locator for Other issues with Sign-In link
driver.find_element(By.ID,'ap-other-signin-issues-link')

# 9. locator forCreate your Amazon account button
driver.find_element(By.ID,'createAccountSubmit')

