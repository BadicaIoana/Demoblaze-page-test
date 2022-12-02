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

# Find the button
chrome.find_element(By.ID,'signin2').click()
sleep(3)

# Insert the keys
chrome.find_element(By.ID,'sign-username').send_keys('ioana29')
sleep(3)

# Insert the keys
chrome.find_element(By.ID,'sign-password').send_keys('ioanamaria29')
sleep(3)

# Press sign in button
chrome.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
sleep(3)

# Verify if the error has displayed
exist_msg = 'This user already exist.'
assert exist_msg == 'This user already exist.'

# Close Chrome
chrome.quit()

# Print the result
print('SUCCESS - TEST PASSED')


