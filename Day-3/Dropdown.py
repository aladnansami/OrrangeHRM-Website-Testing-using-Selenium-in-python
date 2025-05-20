from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

# Create Select object for the country dropdown
drowpdownele = Select(driver.find_element(By.XPATH, "//select[@id='country']"))

# ✅ 1. Select by visible text
drowpdownele.select_by_visible_text("India").click()

# ✅ 2. Select by value (check option HTML value)
#drowpdownele.select_by_value("1")

# ✅ 3. Select by index (starts from 0)
#drowpdownele.select_by_index(13)


# print all option

alloption= drowpdownele.options
print(len(alloption))

#print all option

for optn in alloption:
    print(optn.text)





