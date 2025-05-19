from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#path for chrome driver
chrome_driver_path = r"E:\Automation_Testing\Web_Driver\Chrome_Driver\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demo.nopcommerce.com/register")
driver.get("https://www.amazon.in/")

driver.back()
driver.forward()
driver.refresh()

driver.maximize_window()
print(driver.title)

driver.quit()
