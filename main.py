from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

print("login process activated")

# login credentials
emailStr = ''
passwordStr = ''

# This application runned on chrome 96
# Not tested on the newer chrome versions
browser = webdriver.Chrome()
browser.get(('WEBSITE_URL'))

# email input field (Element in inspector)
mailInput = browser.find_element_by_name('email')
mailInput.send_keys(emailStr)

# password input field (Element in inspector)
password = browser.find_element_by_name('password')
password.send_keys(passwordStr)

# Button field (Element in inspector)
signInButton = browser.find_element_by_xpath("//button[@class='btn btn--orange']")
signInButton.click()

# 
while True:
    print("running...")

    browser.navigate().refresh()
    time.sleep(10)
    

