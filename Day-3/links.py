from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#path for chrome driver
chrome_driver_path = r"E:\Automation_Testing\Web_Driver\Chrome_Driver\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# link
# driver.find_element(By.LINK_TEXT , "Digital downloads").click()

# partial link

driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# find total number of links in a page

total_links = driver.find_elements(By.TAG_NAME,"a")
print(len('total_links'))

#print all link

for link in total_links:
    print(link.text)