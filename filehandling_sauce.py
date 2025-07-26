# file_ = open(file='..\selenium_july13\webpage_task10.txt', mode='w')
# abc = 'This is my handson'
# file_.write(abc)
# file_.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)
curr_url = driver.current_url
curr_title = driver.title
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
content = driver.page_source
# with open("webpage_task10.txt", "w", encoding="utf-8") as file:file.write(content)
file_ = open(file='..\selenium_july13\webpage1_task10.txt', mode='w',encoding="utf-8")
# abc = 'This is my handson'
file_.write(content)
file_.close()
print("Webpage content saved to 'webpage_content_selenium.txt'")


driver.quit()

