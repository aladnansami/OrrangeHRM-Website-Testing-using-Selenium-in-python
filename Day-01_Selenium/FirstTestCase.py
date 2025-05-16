from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Required for By.XXX

# Path to ChromeDriver
chrome_driver_path = r"E:\Automation_Testing\Web_Driver\Chrome_Driver\chromedriver.exe"

# Setup service and options
service = Service(executable_path=chrome_driver_path)
options = Options()

# Launch browser
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait briefly to let elements load (you can improve this with WebDriverWait)
import time
time.sleep(2)

# Use updated locator syntax
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

actual_title = driver.title
expected_title = "OrangeHRM"
if actual_title == expected_title :
    print("Successfully logged in")

else:
    print("Failed to log in")

driver.close()