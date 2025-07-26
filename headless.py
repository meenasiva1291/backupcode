import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

def test_headless():
    try:
        driver_option = Options()
        driver_option.add_argument("--incognito")#alternate: "--headless"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(),options = driver_option))
        driver.get('https://the-internet.herokuapp.com/windows')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[text()='Click Here']").click()
        windows = driver.window_handles
        # print(driver.title)
        for windo in windows:
            driver.switch_to.window(windo)
            windo_title = driver.title
            # assert windo_title == driver.title, "The title is not matching"
            assert windo_title == driver.title, "The title is not matching"
            # time.sleep(2)
            # print(driver.title)
            print(driver.current_url)

    except Exception as e:
        print(e)