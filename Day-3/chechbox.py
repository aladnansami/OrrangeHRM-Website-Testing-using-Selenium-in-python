from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#path for chrome driver
chrome_driver_path = r"E:\Automation_Testing\Web_Driver\Chrome_Driver\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# select specific

# driver.find_element(By.ID,"monday").click()

# all 7 check box

checkboxs = driver.find_elements(By.XPATH, "//input[@type ='checkbox' and contains(@id, 'day')]")

#for i in range(len(checkboxs)):
 #   checkboxs[i].click()


# select multiple checkboxes by choice

for checkbox in checkboxs:
     weekname = checkbox.get_attribute("id")
     if weekname == 'monday' or weekname == 'tuesday' :
         checkbox.click()
         print(weekname)

# select last 2 checkbox


for i in range(len(checkboxs)-2, len(checkboxs)):
    checkboxs[i].click()



# first two selected

for i in range(len(checkboxs)):
    if i <2:
        checkboxs[i].click()

# clear all the checkbox

for checkbox in checkboxs:
    if checkbox.is_selected():
        checkbox.click()

