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
import My_Helpers as HP

fake = Faker()

class Chrome_Puma_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # -----------POSITIVE TESTS-----------

    # Test-Case 1

    def test1_positive_opening_website_url(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Assert that in title "PUMA.com | Forever Faster."

        try:
            assert "PUMA.com | Forever Faster." in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Https protocol: ", HP.url, " is active!")

    def tearDown(self):
        self.driver.quit()

    # Test-Case 2

    def test2_positive_registration_user_account(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Registration User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.register_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_Registr_Account)))
        # Enter First Name, Last Name, Email and Password
        driver.find_element(By.NAME, HP.fake_first_name).send_keys(fake.first_name())
        driver.find_element(By.NAME, HP.fake_last_name).send_keys(fake.last_name())
        # fake email doesn't work
        # You need to change email1 every time you test
        driver.find_element(By.NAME, HP.email_1).send_keys(HP.gmail)
        driver.find_element(By.NAME, HP.fake_password).send_keys(fake.password())
        driver.find_element(By.XPATH, HP.button_submit).click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_My_Account)))
        driver.find_element(By.XPATH, HP.text_My_Accound)

        # Assert that in title "PUMA Online Shop - My account"

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
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.logIn_button).click()
        driver.find_element(By.ID, HP.email_const).send_keys(HP.gmail_const)
        driver.find_element(By.ID, HP.password_const).send_keys(HP.password)
        driver.find_element(By.XPATH, HP.button_login_submit).click()

        time.sleep(3)

        # Assert that in title "PUMA Online Shop - My account"

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        # Sign out

        driver.find_element(By.ID, HP.account_button).click()
        time.sleep(3)
        driver.find_element(By.XPATH, HP.logOut_button).click()

    def tearDown(self):
        self.driver.quit()

    # Test-Case 4

    def test4_positive_address_book(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.logIn_button).click()
        driver.find_element(By.ID, HP.email_const).send_keys(HP.gmail_const)
        driver.find_element(By.ID, HP.password_const).send_keys(HP.password)
        driver.find_element(By.XPATH, HP.button_login_submit).click()

        time.sleep(6)

        # Assert that in title "PUMA Online Shop - My account"

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        # Add address book

        driver.find_element(By.XPATH, HP.add_new_address).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_new_address)))
        driver.find_element(By.ID, HP.address_title_input).send_keys(HP.address_title)
        driver.find_element(By.XPATH, HP.country).click()
        driver.find_element(By.ID, HP.first_name).send_keys(fake.first_name())
        driver.find_element(By.ID, HP.last_name).send_keys(fake.last_name())
        driver.find_element(By.ID, HP.address1).send_keys(HP.address)
        driver.find_element(By.ID, HP.city_input).send_keys(HP.city)
        driver.find_element(By.ID, HP.postalCode).send_keys(HP.postalCode)
        driver.find_element(By.XPATH, HP.state).click()
        driver.find_element(By.ID, HP.phone_input).send_keys(HP.phone_number)
        # Make default address
        driver.find_element(By.ID, HP.button_default_address).click()
        # Submit
        driver.find_element(By.XPATH, HP.button_submit_contains).click()

        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_menu_address)))

        # Check that we are back in your account

        # Assert that in title "PUMA Online Shop - My account"

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("New address added!")

        # Sign out

        driver.find_element(By.ID, HP.account_button).click()
        time.sleep(3)
        driver.find_element(By.XPATH, HP.logOut_button).click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    # Test-Case 5

    def test5_positive_edit_address_in_book(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.logIn_button).click()
        driver.find_element(By.ID, HP.email_const).send_keys(HP.gmail_const)
        driver.find_element(By.ID, HP.password_const).send_keys(HP.password)
        driver.find_element(By.XPATH, HP.button_login_submit).click()

        time.sleep(6)

        # Assert that in title "PUMA Online Shop - My account"

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        # Change address book

        driver.find_element(By.XPATH, HP.button_edit_address).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_new_address)))
        addressTitle = driver.find_element(By.ID, HP.address_title_input)
        addressTitle.clear()
        addressTitle.send_keys(HP.address_title_new)
        address1 = driver.find_element(By.ID, HP.address1)
        address1.clear()
        address1.send_keys(HP.address_new)
        postalcode = driver.find_element(By.ID, HP.postalCode)
        postalcode.clear()
        postalcode.send_keys(HP.postal_code_new)
        driver.find_element(By.XPATH, HP.button_submit_contains).click()

        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_menu_address_change)))

        # Assert that in title "PUMA Online Shop - Address Book"

        try:
            assert "PUMA Online Shop - Address Book" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)
        print("Edit address!")

        # Back to my Account

        driver.find_element(By.XPATH, HP.back_to_account).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_menu_address)))

        # Check that we are back in your account

        # Assert that in title "PUMA Online Shop - My account"

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)


        # Sign out

        driver.find_element(By.ID, HP.account_button).click()
        time.sleep(3)
        driver.find_element(By.XPATH, HP.logOut_button).click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    # Test-Case 6

    def test6_positive_add_item_to_card(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Sign in User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.logIn_button).click()
        driver.find_element(By.ID, HP.email_const).send_keys(HP.gmail_const)
        driver.find_element(By.ID, HP.password_const).send_keys(HP.password)
        driver.find_element(By.XPATH, HP.button_login_submit).click()

        time.sleep(6)

        # Assert that in title "PUMA Online Shop - My account"

        try:
            assert "PUMA Online Shop - My account" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        print("Logged in to your account")

        # Suede Classic XXI Sneakers add to cart

        driver.find_element(By.XPATH, HP.section_men).click()
        time.sleep(2)
        driver.find_element(By.XPATH, HP.type_of_shoe).click()
        time.sleep(2)
        driver.find_element(By.XPATH, HP.suede_classic).click()
        time.sleep(2)
        driver.find_element(By.XPATH, HP.size).click()
        driver.find_element(By.XPATH, HP.button_add_to_cart).click()
        time.sleep(2)
        driver.find_element(By.XPATH, HP.added_to_cart)
        print("Suede Classic XXI Sneakers added to cart!")
        time.sleep(1)

        # Suede Classic XXI Sneakers add to cart

        driver.find_element(By.XPATH, HP.open_cart).click()
        driver.find_element(By.XPATH, HP.cart_title)
        driver.find_element(By.XPATH, HP.shoes_in_cart)

        print("The item is in the cart!")

    def tearDown(self):
        self.driver.quit()

    # -----------NEGATIVE TESTS-----------

    # ----------Test-Case 1----------

    def test1_negative_incorrect_email(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Registration User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.register_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_Registr_Account)))

        # Assert that in title "PUMA Online Shop - Account Register"

        try:
            assert "PUMA Online Shop - Account Register" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        # Enter First Name, Last Name, Email and Password
        driver.find_element(By.NAME, HP.fake_first_name).send_keys(fake.first_name())
        driver.find_element(By.NAME, HP.fake_last_name).send_keys(fake.last_name())
        driver.find_element(By.NAME, HP.email_1).send_keys(HP.incor_email)
        driver.find_element(By.NAME, HP.fake_password).send_keys(fake.password())
        driver.find_element(By.XPATH, HP.button_submit).click()
        time.sleep(3)

        try:
            driver.find_element(By.XPATH, HP.registration_form_error)
            print("Negative Test PASSED. You need to have a valid email!")
        except WDE:
            print("Negative Test FALSE. Account created!")

    def tearDown(self):
        self.driver.quit()


    # ----------Test-Case 2----------

    def test2_negative_incorrect_password(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Registration User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.register_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_Registr_Account)))

        # Assert that in title "PUMA Online Shop - Account Register"

        try:
            assert "PUMA Online Shop - Account Register" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        # Enter First Name, Last Name, Email and Password
        driver.find_element(By.NAME, HP.fake_first_name).send_keys(fake.first_name())
        driver.find_element(By.NAME, HP.fake_last_name).send_keys(fake.last_name())
        driver.find_element(By.NAME, HP.email_1).send_keys(HP.gmail2)
        driver.find_element(By.NAME, HP.fake_password).send_keys(HP.incor_password)
        driver.find_element(By.XPATH, HP.button_submit).click()
        time.sleep(3)

        try:
            driver.find_element(By.XPATH, HP.registration_form_error)
            print("Negative Test PASSED. You need to have a valid Password!")
        except WDE:
            print("Negative Test FALSE. Account created!")

    def tearDown(self):
        self.driver.quit()

    # ----------Test-Case 3----------

    def test3_negative_empty_email(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Registration User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.register_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_Registr_Account)))

        # Assert that in title "PUMA Online Shop - Account Register"

        try:
            assert "PUMA Online Shop - Account Register" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        # Enter First Name, Last Name, Email and Password
        driver.find_element(By.NAME, HP.fake_first_name).send_keys(fake.first_name())
        driver.find_element(By.NAME, HP.fake_last_name).send_keys(fake.last_name())
        driver.find_element(By.NAME, HP.email_1).send_keys(HP.gmail3)
        driver.find_element(By.NAME, HP.fake_password).send_keys(fake.password())
        driver.find_element(By.XPATH, HP.button_submit).click()
        try:
            driver.find_element(By.XPATH, HP.registration_error)
            print("Negative Test PASSED. You need to have a valid email!")
        except WDE:
            print("Negative Test FALSE. Account created!")

    def tearDown(self):
        self.driver.quit()

    # ----------Test-Case 4----------

    def test4_negative_empty_password(self):
        driver = self.driver
        driver.get(HP.url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.menu_bar)))
        # Close pop-up message 1
        driver.find_element(By.XPATH, HP.popUp_message_1).click()
        # Close pop-up message 2
        driver.find_element(By.XPATH, HP.popUp_message_2).click()
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # Registration User Account

        driver.find_element(By.ID, HP.account_button).click()
        driver.find_element(By.XPATH, HP.register_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.wait_Registr_Account)))

        # Assert that in title "PUMA Online Shop - Account Register"

        try:
            assert "PUMA Online Shop - Account Register" in driver.title
            print("The title is correct: ", driver.title)
        except AssertionError:
            print("The title is not correct. The title is: ", driver.title)

        # Enter First Name, Last Name, Email and Password
        driver.find_element(By.NAME, HP.fake_first_name).send_keys(fake.first_name())
        driver.find_element(By.NAME, HP.fake_last_name).send_keys(fake.last_name())
        driver.find_element(By.NAME, HP.email_1).send_keys(HP.gmail4)
        driver.find_element(By.NAME, HP.fake_password).send_keys(HP.empty_password)
        driver.find_element(By.XPATH, HP.button_submit).click()
        try:
            driver.find_element(By.XPATH, HP.registration_error)
            #driver.find_element(By.XPATH, HP.registration_error_1)
            print("Negative Test PASSED. You need to have a valid Password!")
        except WDE:
            print("Negative Test FALSE. Account created!")

    def tearDown(self):
        self.driver.quit()

