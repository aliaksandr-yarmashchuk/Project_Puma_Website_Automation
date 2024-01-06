from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.common.keys import Keys

# ----------Website address----------

url = "https://us.puma.com/us/en"

# ----------All Test-Cases and Test-Case 1----------

menu_bar = "//ul[contains(@role,'menubar')]"  # XPath
popUp_message_1 = "//button[contains(@data-test-id,'stay-on-region-button')]"  # Location
popUp_message_2 = "(//div[contains(@data-uds-child,'action-icon-icon')])[1]"  # Website uses Cookies
account_button = "account-button"  # ID

# ----------Test-Case 2----------

# Registration User Account:

register_button = "//a[@data-test-id='register-button']"  # XPath
wait_Registr_Account = "//p[contains(.,'My account')]"  # XPath
fake_first_name = "firstName"  # NAME
fake_last_name = "lastName"  # NAME
email_1 = "email"  # NAME
# You need to change email1 every time you test
gmail = "hgjtkdhshe@gmail.com"
fake_password = "password"  # NAME
button_submit = "//button[@type='submit']"  # XPath
wait_My_Account = "(//div[contains(@data-uds-child,'stack')])[2]"  # XPath
text_My_Accound = "//span[contains(text(),'My account')]"  # XPath

# ----------Test-Case 3----------

logIn_button = "//a[@data-test-id='login-button']"  # XPath
email_const = "email"  # ID
gmail_const = "ivanov.alexander@gmail.com"
password_const = "password"  # ID
password = "Test123456"
button_login_submit = "//button[@id='login-submit']"  # XPath
logOut_button = "//button[@data-test-id='logout-button']"  # XPath

# ----------Test-Case 4----------

# logIn_button, email_const, gmail_const, password_const, password, button_login_submit, logOut_button in Test-Case 3

add_new_address = "//a[@data-test-id='add-new-address']"  # XPath
wait_new_address = "//div[@class='tw-10v7mpc tw-1p4ksvz']"  # XPath
address_title_input = "address-title-input"  # ID
address_title = "2 Wall Street, NY"  # ID
country = "//option[contains(text(),'United States')]"  # XPath
first_name = "firstName-input"  # ID
last_name = "lastName-input"  # ID
address1 = "address1"  # ID
address = "2 Wall Street"
city_input = "city-input"  # ID
city = "New York"
postalCode = "postalCode-input"  # ID
postal_code = "10005"
state = "//option[contains(text(),'New York')]"  # XPath
phone_input = "phone-input"  # ID
phone_number = "+14845524458"
button_default_address = "preferred-address"  # ID
button_submit_contains = "//button[contains(@type,'submit')]"  # XPath
wait_menu_address = "//address[contains(@data-test-id,'address-information')]"  # XPath

# ----------Test-Case 5----------

# logIn_button, email_const, gmail_const, password_const, password, button_login_submit, logOut_button in Test-Case 3
# wait_new_address, address_title_input, address1, postalCode, button_submit_contains, wait_menu_address  in Test-Case 4

button_edit_address = "//a[contains(@data-test-id,'edit-address')]"  # XPath
address_title_new = "Broadway, New York"
address_new = "1567 Broadway, New York"
postal_code_new = "10036"
wait_menu_address_change = "//div[contains(@class,'tw-pa7mf4 tw-1p4ksvz')]"  # XPath
back_to_account = "//div[contains(text(),'Back to my account')]"  # XPath

# ----------Test-Case 6----------

# logIn_button, email_const, gmail_const, password_const, password, button_login_submit, logOut_button in Test-Case 3




