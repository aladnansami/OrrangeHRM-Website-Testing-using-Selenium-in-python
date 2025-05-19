from faulthandler import is_enabled
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#path for chrome driver
chrome_driver_path = r"E:\Automation_Testing\Web_Driver\Chrome_Driver\chromedriver.exe"

# Setup service and options

service = Service(executable_path=chrome_driver_path)
options = Options()


# Launch browser
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://testautomationpractice.blogspot.com/") #opening the applicationurl
driver.maximize_window()

# Wait briefly to let elements load (you can improve this with WebDriverWait)
import time
time.sleep(2)

# Use updated locator syntax
#Application Commands
print(driver.title) # show title of the current title
print(driver.current_url) # show the current url
print(driver.page_source) # show the page source
driver.find_element(By.ID,"name").send_keys("Al Adnan Sami")
driver.find_element(By.ID,"email").send_keys("aladnansami21@gmail.com")
driver.find_element(By.ID,"phone").send_keys("01620208031")
driver.find_element(By.ID,"textarea").send_keys("312/1,SOUTHPAIKPARA,MIRPUR01")

# select radio button for male
male_ratio = driver.find_element(By.ID,"male")
female_ratio = driver.find_element(By.ID,"female")

male_ratio.click()

#Conditional commands
#is_enabled()
#is_displayed()
#is.selected()


