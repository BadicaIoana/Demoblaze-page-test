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

# Find the add to cart button
chrome.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
sleep(3)

# Press the button
chrome.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()
sleep(3)

# Verify if the product has added
Add_btn = 'Product added'
assert (False), 'Product added'

# Close Chrome
chrome.quit()

# Print the result
print('SUCCESS - TEST PASSED')