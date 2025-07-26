import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(2)
driver.get("https://formy-project.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Auto").click()
time.sleep(3)
driver.find_element(By.ID,"autocomplete").send_keys("Merchandise street")
driver.find_element(By.ID,"street_number").send_keys("222")
# driver.find_element(By.XPATH,"//input[@placeholder='Street address 2']").click()#send_keys throwing error while using this xpath
driver.find_element(By.ID,"route").send_keys("Ilinios")
driver.find_element(By.ID,"locality").send_keys("chicago")
driver.find_element(By.ID,"administrative_area_level_1").send_keys("california")
driver.find_element(By.ID,"postal_code").send_keys("60654")
driver.find_element(By.ID,"country").send_keys("USA")
driver.quit()
