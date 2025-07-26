import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.guvi.in/")
driver.find_element(By.ID,"login-btn").click()
time.sleep(2)
driver.find_element(By.ID,"email").send_keys("meenakshisivasankar@gmail.com")
driver.find_element(By.ID,"password").send_keys("Meenu1291")
curr_url = driver.current_url
print(curr_url)

def test_PositiveTC01ValidateURL():
    try:
        assert curr_url == "https://www.guvi.in/sign-in/", "Expected URL not matching"
        # driver.find_element(By.)
        # time.sleep(3)


    finally:
        driver.quit()