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
file_ = open(file='..\selenium_july13\Webpage_task_11.txt', mode='w',encoding="utf-8")
# abc = 'This is my handson'
file_.write(content)
file_.close()

print("Webpage content saved to 'webpage_content_selenium.txt'")

curr_url1 = driver.current_url
curr_title1 = driver.title


def test_PositiveURLTc01_HomePage():
    try:
        print(curr_url)
        print(curr_title)
        assert curr_url == "https://www.saucedemo.com/", "Expected URL not matching"
    finally:
        driver.quit()

def test_PositiveTitleTc02_HomePage():
    try:
        print(curr_url)
        print(curr_title)
        assert curr_title == "Swag Labs", "Expected URL not matching"
    finally:
        driver.quit()

def test_NegativeURLTc03_HomePage():
    try:
        print(curr_url)
        print(curr_title)
        assert curr_url == "https://www.guvis.in/sign-in/", "Expected URL not matching"
    finally:
        driver.quit()

def test_NegativeTitleTc04_HomePage():
    try:
        print(curr_url)
        print(curr_title)
        assert curr_title == "GUVI LAB", "Expected URL not matching"
    finally:
        driver.quit()

def test_PositiveURLTc01_Dashboard():
    try:
        print(curr_url1)
        print(curr_title1)
        assert curr_url1 == "https://www.saucedemo.com/inventory.html", "Expected URL not matching"
    finally:
        driver.quit()

def test_PositiveTitleTc02_Dashboard():
    try:
        print(curr_url1)
        print(curr_title1)
        assert curr_title1 == "Swag Labs", "Expected URL not matching"
    finally:
        driver.quit()

def test_NegativeURLTc03_Dashboard():
    try:
        print(curr_url1)
        print(curr_title1)
        assert curr_url1 == "https://www.saucedemo2.com/inventory.html", "Expected URL not matching"
    finally:
        driver.quit()

def test_NegativeTitleTc04_Dashboard():
    try:
        print(curr_url1)
        print(curr_title1)
        assert curr_title1 == "GUVI LAB", "Expected URL not matching"
    finally:
        driver.quit()


