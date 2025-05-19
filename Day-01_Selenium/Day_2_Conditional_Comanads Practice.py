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
driver.maximize_window()
print(driver.title)

#is_displayd and is_enebled

searchbox = driver.find_element(By.ID, "small-searchterms")

print("Display Status", searchbox.is_displayed())
print("Enabled Status", searchbox.is_enabled())

#is_selected we can use for radio button

radio_male =  driver.find_element(By.ID, "gender-male")
radio_female = driver.find_element(By.ID, "gender-female")

print("Male selected: ",radio_male.is_selected())
print("Female selected: ", radio_female.is_selected())

radio_male.click()
#After selecting radio button male radio button
print("Male selected: ", radio_male.is_selected())

print("Female selected: ", radio_female.is_selected())

