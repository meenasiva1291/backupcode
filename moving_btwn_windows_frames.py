import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Windows.html")
time.sleep(5)
driver.find_element(By.CLASS_NAME,'get btn btn-primary').click()
time.sleep(5)
driver.quit()


