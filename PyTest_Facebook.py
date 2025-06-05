import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
import time
from selenium.common.exceptions import WebDriverException as WDE
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

fake = Faker()

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    yield driver
    driver.quit()

def test_positive_open_url_facebook(driver):
    driver.get("https://www.facebook.com")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'_al67')]")))
    time.sleep(2)
    # Pop-Up Message
    driver.find_element(By.XPATH, "(//div[contains(.,'Разрешить все cookie')])[18]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
    driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(fake.password())
    time.sleep(10)





'''
def test01_positive_registration_user_account(self):
заменяем на:
def test_positive_registration_user_account(driver):
assert, except:
try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Account created!")
        
заменяем на:
assert "PUMA Online Shop - My account" in driver.title, f"Incorrect title: {driver.title}"
print("The title is correct: ", driver.title)
print("Account created!")
'''
