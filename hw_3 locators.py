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
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dlog%2Binto%2Bmy%2Baccount%26adgrpid%3D1342504260767739%26hvadid%3D83906587170637%26hvbmt%3Dbb%26hvdev%3Dc%26hvlocphy%3D77332%26hvnetw%3Do%26hvqmt%3Db%26hvtargid%3Dkwd-83906857989942%253Aloc-190%26hydadcr%3D18897_10527797%26msclkid%3Dbaa0b59f174c1d54224fd3064e5fc71a%26tag%3Dmh0b-20%26ref%3Dnav_ya_signin&prevRID=P4E7PRJ4P2SP1CGP0RY8&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# 1. locator for Amazon logo
driver.find_element(By.CSS_SELECTOR,".a-icon.a-icon-logo")

# 2. Locator for Create Account
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")

# 3. locator for Your name field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# 4. locator for Mobile number or email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# 5.  locator for Password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# 6. locator for Re-enter password field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# 7. locator for continue button
driver.find_element(By.CSS_SELECTOR, "input.a-button-input")

# 8. locator for Conditions of use link
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")

# 9. loactor for Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")

# 10. locator for Signin link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")
