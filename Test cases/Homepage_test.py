from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Initialize the chrome driver
chrome = webdriver.Chrome()

# Go to url
chrome.get('https://www.demoblaze.com/index.html#')

# Maximize
chrome.maximize_window()
sleep(3)

# Press the homepage button
chrome.find_element(By.ID,'nava').click()
sleep(3)

# Verify if the button has pressed
homepage_btn = 'homepage'
assert (False), 'homepage'

# Close Chrome
chrome.quit()

# Print the result
print('SUCCESS - TEST PASSED')