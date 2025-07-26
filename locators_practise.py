import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
time.sleep(5)
driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt").click()#id(#),class(.)->option 1
time.sleep(5)
driver.find_element(By.XPATH,"//button[@name='add-to-cart-sauce-labs-fleece-jacket']").click()
time.sleep(5)
# driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']").click() # option 2
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"Faceb").click()
time.sleep(10)
curr_url = driver.current_url
print(curr_url)
assert curr_url == "https://www.guvis.in/sign-in/", "Expected URL not matching"
driver.quit()

