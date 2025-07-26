# from selenium import webdriver
# driver = webdriver.Edge()
# driver.get("https://www.google.com/")
# print(driver.title)
# driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

print(driver.current_url) #optional
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Below is the sythax for navigating page handles
# time.sleep(10)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
driver.quit()





