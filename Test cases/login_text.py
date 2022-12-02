from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Initialize the chrome driver
chrome = webdriver.Chrome()

# Go to url
chrome.get('https://www.demoblaze.com/index.html#')

# Maximize
chrome.maximize_window()
sleep(3)

# Find the login button
chrome.find_element(By.ID,'login2').click()
sleep(3)

# Insert the keys
chrome.find_element(By.ID,'loginusername').send_keys('ioana29')
sleep(3)

# Insert the keys
chrome.find_element(By.ID,'loginpassword').send_keys('ioanamaria29')
sleep(3)

# Press log in button
chrome.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
sleep(3)

# Verify if the log in button has pressed
log_in_btn = 'Log in'
assert log_in_btn == 'Log in'

# Close Chrome
chrome.quit()

# Print the result
print('SUCCESS - TEST PASSED')

