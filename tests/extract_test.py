from selenium import webdriver
from selenium.webdriver.common.by import By

print("Test Execution Started")

options = webdriver.FirefoxOptions()
options.add_argument('--web-security=no')
options.add_argument('--ssl-protocol=any')
options.add_argument('--ignore-ssl-errors=yes')

driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)

print ("Checking extract")
driver.get('http://frontend/extract')
print (driver.find_element(By.TAG_NAME, "title").get_attribute('innerText'))

print ("Checking geoshop")
driver.get('http://frontend/geoshop')
print (driver.find_element(By.TAG_NAME, "title").get_attribute('innerText'))

driver.close()
print("Test Execution Completed")