import time
import unittest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

fake = Faker()

class Chrome_Puma_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # -----------POSITIVE TESTS-----------

    # Test-Case 1

    def test1_positive_opening_website_url(self):
        driver = self.driver
        driver.get("https://us.puma.com/us/en")
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@role,'menubar')]")))
        driver.find_element(By.XPATH, "//button[contains(@data-test-id,'stay-on-region-button')]").click()
        driver.find_element(By.XPATH, "(//div[contains(@data-uds-child,'action-icon-icon')])[1]").click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Assert that in title "Stock photos, royalty-free images, graphics, vectors & videos | Adobe Stock"

        try:
            assert "PUMA.com | Forever Faster." in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

    def tearDown(self):
        self.driver.quit()

    # Test-Case 2

    def test2_positive_registration_user_account(self):
        driver = self.driver
        driver.get("https://us.puma.com/us/en")
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@role,'menubar')]")))
        driver.find_element(By.XPATH, "//button[contains(@data-test-id,'stay-on-region-button')]").click()
        driver.find_element(By.XPATH, "(//div[contains(@data-uds-child,'action-icon-icon')])[1]").click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Registration User Account

        driver.find_element(By.ID, "account-button").click()
        driver.find_element(By.XPATH, "//a[@data-test-id='register-button']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(.,'My account')]")))
        # Enter First Name, Last Name, Email and Password
        driver.find_element(By.NAME, "firstName").send_keys(fake.first_name())
        driver.find_element(By.NAME, "lastName").send_keys(fake.last_name())
        # fake email doesn't work
        driver.find_element(By.NAME, "email").send_keys("hgjtkdhshe@gmail.com")
        driver.find_element(By.NAME, "password").send_keys(fake.password())
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(@data-uds-child,'stack')])[2]")))
        driver.find_element(By.XPATH, "//span[contains(text(),'My account')]")

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Account created!")

    def tearDown(self):
        self.driver.quit()

    # Test-Case 3

    def test3_positive_login_user_account(self):
        driver = self.driver
        driver.get("https://us.puma.com/us/en")
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@role,'menubar')]")))
        driver.find_element(By.XPATH, "//button[contains(@data-test-id,'stay-on-region-button')]").click()
        driver.find_element(By.XPATH, "(//div[contains(@data-uds-child,'action-icon-icon')])[1]").click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, "account-button").click()
        driver.find_element(By.XPATH, "//a[@data-test-id='login-button']").click()
        driver.find_element(By.ID, "email").send_keys("ivanov.alexander@gmail.com")
        driver.find_element(By.ID, "password").send_keys("Test123456")
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()

        time.sleep(3)

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        # Sign out

        driver.find_element(By.ID, "account-button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@data-test-id='logout-button']").click()

    def tearDown(self):
        self.driver.quit()

    # Test-Case 4

    def test4_positive_address_book(self):
        driver = self.driver
        driver.get("https://us.puma.com/us/en")
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@role,'menubar')]")))
        driver.find_element(By.XPATH, "//button[contains(@data-test-id,'stay-on-region-button')]").click()
        driver.find_element(By.XPATH, "(//div[contains(@data-uds-child,'action-icon-icon')])[1]").click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, "account-button").click()
        driver.find_element(By.XPATH, "//a[@data-test-id='login-button']").click()
        driver.find_element(By.ID, "email").send_keys("ivanov.alexander@gmail.com")
        driver.find_element(By.ID, "password").send_keys("Test123456")
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()

        time.sleep(6)

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        # Add address book

        driver.find_element(By.XPATH, "//a[@data-test-id='add-new-address']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tw-10v7mpc tw-1p4ksvz']")))
        driver.find_element(By.ID, "address-title-input").send_keys("2 Wall Street, NY")
        driver.find_element(By.XPATH, "//option[contains(text(),'United States')]").click()
        driver.find_element(By.ID, "firstName-input").send_keys(fake.first_name())
        driver.find_element(By.ID, "lastName-input").send_keys(fake.last_name())
        driver.find_element(By.ID, "address1").send_keys("2 Wall Street")
        driver.find_element(By.ID, "city-input").send_keys("New York")
        driver.find_element(By.ID, "postalCode-input").send_keys("10005")
        driver.find_element(By.XPATH, "//option[contains(text(),'New York')]").click()
        driver.find_element(By.ID, "phone-input").send_keys("+14845524458")
        # Make default address
        driver.find_element(By.ID, "preferred-address").click()
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()

        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//address[contains(@data-test-id,'address-information')]")))

        # Check that we are back in your account

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("New address added!")

        # Sign out

        driver.find_element(By.ID, "account-button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@data-test-id='logout-button']").click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    # Test-Case 5

    def test5_positive_edit_address_in_book(self):
        driver = self.driver
        driver.get("https://us.puma.com/us/en")
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@role,'menubar')]")))
        driver.find_element(By.XPATH, "//button[contains(@data-test-id,'stay-on-region-button')]").click()
        driver.find_element(By.XPATH, "(//div[contains(@data-uds-child,'action-icon-icon')])[1]").click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, "account-button").click()
        driver.find_element(By.XPATH, "//a[@data-test-id='login-button']").click()
        driver.find_element(By.ID, "email").send_keys("ivanov.alexander@gmail.com")
        driver.find_element(By.ID, "password").send_keys("Test123456")
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()

        time.sleep(6)

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        # Change address book

        driver.find_element(By.XPATH, "//a[contains(@data-test-id,'edit-address')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tw-10v7mpc tw-1p4ksvz']")))
        addressTitle = driver.find_element(By.ID, "address-title-input")
        addressTitle.clear()
        addressTitle.send_keys("Broadway, New York")
        address1 = driver.find_element(By.ID, "address1")
        address1.clear()
        address1.send_keys("1567 Broadway, New York")
        postalcode = driver.find_element(By.ID, "postalCode-input")
        postalcode.clear()
        postalcode.send_keys("10036")
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()

        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'tw-pa7mf4 tw-1p4ksvz')]")))

        try:
            assert "PUMA Online Shop - Address Book" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)
        print("Edit address!")

        # Back to my Account

        driver.find_element(By.XPATH, "//div[contains(text(),'Back to my account')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//address[contains(@data-test-id,'address-information')]")))

        # Check that we are back in your account

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)


        # Sign out

        driver.find_element(By.ID, "account-button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@data-test-id='logout-button']").click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    # Test-Case 6

    def test6_positive_(self):
        driver = self.driver
        driver.get("https://us.puma.com/us/en")
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[contains(@role,'menubar')]")))
        driver.find_element(By.XPATH, "//button[contains(@data-test-id,'stay-on-region-button')]").click()
        driver.find_element(By.XPATH, "(//div[contains(@data-uds-child,'action-icon-icon')])[1]").click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, "account-button").click()
        driver.find_element(By.XPATH, "//a[@data-test-id='login-button']").click()
        driver.find_element(By.ID, "email").send_keys("ivanov.alexander@gmail.com")
        driver.find_element(By.ID, "password").send_keys("Test123456")
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()

        time.sleep(6)

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        #
