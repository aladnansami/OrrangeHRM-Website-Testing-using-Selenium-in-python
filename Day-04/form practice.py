from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#path for chrome driver
chrome_driver_path = r"E:\Automation_Testing\Web_Driver\Chrome_Driver\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

name =  driver.find_element(By.ID, "name").send_keys("Md Al Adnan")
email = driver.find_element(By.ID, "email").send_keys("aladnansami21@gmail.com")
phone = driver.find_element(By.ID, "phone").send_keys("01625208031")
textarea = driver.find_element(By.ID, "textarea").send_keys("ami practice kortechi")
male_radio = driver.find_element(By.ID, "male").click()

checkboxs = driver.find_elements(By.XPATH, "//input[@type ='checkbox' and contains(@id, 'day')]")

for checkbox in checkboxs:
     weekname = checkbox.get_attribute("id")
     if weekname == 'monday' or weekname == 'tuesday' :
         checkbox.click()
         print(weekname)

# Create Select object for the country dropdown
drowpdownele = Select(driver.find_element(By.XPATH, "//select[@id='country']"))

# ✅ 1. Select by visible text
drowpdownele.select_by_visible_text("India")


# Create Select object for the country dropdown
drowpdownele = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))

# ✅ 1. Select by visible text
drowpdownele.select_by_visible_text("Green")

print(drowpdownele.select_by_visible_text("Red"))

