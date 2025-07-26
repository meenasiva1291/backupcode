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
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"Butt").click()
time.sleep(4)
driver.find_element(By.XPATH,"//button[text()='Primary']").click()
driver.find_element(By.XPATH,"//button[text()='Success']").click()
driver.find_element(By.XPATH,"//button[text()='Info']").click()
driver.find_element(By.XPATH,"//button[text()='Warning']").click()
driver.find_element(By.XPATH,"//button[text()='Danger']").click()
driver.find_element(By.CSS_SELECTOR,".btn-link").click()
driver.find_element(By.XPATH,"//button[text()='Left']").click()
driver.find_element(By.XPATH,"//button[text()='Middle']").click()
driver.find_element(By.XPATH,"//button[text()='Right']").click()
driver.find_element(By.XPATH,"//button[text()='1']").click()
driver.find_element(By.XPATH,"//button[text()='2']").click()
driver.find_element(By.CSS_SELECTOR,".btn-primary dropdown-toggle").click()
driver.find_element(B
# driver.find_element(By.CLASSy_NAME,"btn btn-lg btn-warning").click()
# driver.find_element(By.XPATH,"/button[text()='Danger']").click()
# driver.find_element(By.CLASS_NAME,"btn btn-lg btn-link").click()
time.sleep(5)
driver.quit()
