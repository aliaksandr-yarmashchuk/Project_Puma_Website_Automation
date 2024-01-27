# ----------Website address----------

url = "https://us.puma.com/us/en"

# **********POSITIVE TESTS**********

# ----------All Test-Cases and Test-Case 1----------

menu_bar = "//ul[contains(@role,'menubar')]"  # XPath
popUp_message_1 = "//button[contains(@data-test-id,'stay-on-region-button')]"  # Location
popUp_message_2 = "(//div[contains(@data-uds-child,'text-label')])[7]"  # Website uses Cookies
account_button = "account-button"  # ID

# ----------Test-Case 2----------

# Registration User Account:

register_button = "//a[contains(@data-test-id,'register-button')]"  # XPath
wait_Registr_Account = "//p[contains(.,'My account')]"  # XPath
fake_first_name = "firstName"  # NAME
fake_last_name = "lastName"  # NAME
email_1 = "email"  # NAME
# You need to change email every time you test
gmail = "qwebwqryth@gmail.com"
gmail_edge = "iertyuiertr@gmail.com"
gmail_safari = "byryrrtytysr@gmail.com"
fake_password = "password"  # NAME
button_submit = "//button[@type='submit']"  # XPath
wait_My_Account = "(//div[contains(@data-uds-child,'stack')])[2]"  # XPath
text_My_Accound = "//span[contains(.,'My account')]"  # XPath

# ----------Test-Case 3----------

logIn_button = "//a[@data-test-id='login-button']"  # XPath
email_const = "email"  # ID
gmail_const = "bakyn.aliaksandr@yahoo.com"
password_const = "password"  # ID
password = "Bialenik1234"
button_login_submit = "//button[@id='login-submit']"  # XPath
logOut_button = "//button[@data-test-id='logout-button']"  # XPath

# ----------Test-Case 4----------

# logIn_button, email_const, gmail_const, password_const, password, button_login_submit, logOut_button in Test-Case 3

add_new_address = "//a[@data-test-id='add-new-address']"  # XPath
wait_new_address = "//div[@class='tw-10v7mpc tw-1p4ksvz']"  # XPath
address_title_input = "address-title-input"  # ID
address_title_chrome = "2 Wall Street, NY"
address_title_edge = "3 Wall Street, NY"
address_title_safari = "4 Wall Street, NY"
country = "//option[contains(text(),'United States')]"  # XPath
country_safari1 = "//*[@id='address-form-country-select']"
country_safari2 = "//*[@id='address-form-country-select']/option[2]"
first_name = "firstName-input"  # ID
last_name = "lastName-input"  # ID
address1 = "address1"  # ID
address_chrome = "2 Wall Street"
address_edge = "3 Wall Street"
address_safari = "4 Wall Street"
city_input = "city-input"  # ID
city = "New York"
postalCode = "postalCode-input"  # ID
postal_code_chrome = 10003
postal_code_edge = 10004
postal_code_safari = 10005
state = "//option[contains(text(),'New York')]"  # XPath
state_safari1 = "//select[@id='address-form-state-select']"
state_safari2 = "//option[contains(text(),'New York')]"
phone_input = "phone-input"  # ID
phone_number_chrome = "+14845524458"
phone_number_edge = "+14845524459"
phone_number_safari = "+14845524460"
button_default_address = "preferred-address"  # ID
button_submit_contains = "//button[contains(@type,'submit')]"  # XPath
wait_Dashboard = "//p[@class='tw-1xl28s9 tw-1p4ksvz'][contains(.,'My accountDashboard')]"
wait_menu_address = "//address[contains(@data-test-id,'address-information')]"  # XPath

# ----------Test-Case 5----------

# logIn_button, email_const, gmail_const, password_const, password, button_login_submit, logOut_button in Test-Case 3
# wait_new_address, address_title_input, address1, postalCode, button_submit_contains, wait_menu_address  in Test-Case 4

button_edit_address = "//a[contains(@data-test-id,'edit-address')]"  # XPath
button_edit_address_chrome = "//div[contains(text(),'Edit address 2 Wall Street, NY')]"   # XPath
button_edit_address_edge = "//div[contains(text(),'Edit address 3 Wall Street, NY')]"
button_edit_address_safari = "//*[@id='puma-skip-here']/div[1]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/a"
address_title_new_chrome = "Broadway 1, New York"
address_title_new_edge = "Broadway 2, New York"
address_title_new_safari = "Broadway 3, New York"
address_new_chrome = "1567 Broadway, New York"
address_new_edge = "1568 Broadway, New York"
address_new_safari = "1569 Broadway, New York"
postal_code_new_chrome = 10036
postal_code_new_edge = 10037
postal_code_new_safari = 10038
wait_menu_address_change = "//div[contains(@class,'tw-pa7mf4 tw-1p4ksvz')]"  # XPath
back_to_account = "//div[contains(text(),'Back to my account')]"  # XPath

# **********NEGATIVE TESTS**********

# ----------Test-Case 1----------

# register_button, wait_Registr_Account, fake_first_name, fake_last_name, email_1, fake_password, button_submit, wait_My_Account, text_My_Accound in Positive Test-Case 2 and registration_form_error in Negative Test-Case 1

incor_email = "tupkcts.def@mail"
registration_form_error = "//div[@data-test-id='registration-form-error']"  # XPath

# ----------Test-Case 2----------

# register_button, wait_Registr_Account, fake_first_name, fake_last_name, email_1, fake_password, button_submit, wait_My_Account, text_My_Accound in Positive Test-Case 2
# You need to change email every time you test
gmail2 = "ukkpoietewquj@gmail.com"
gmail_edge2 = "bbwertyutyhs@gmail.com"
gmail_safari2 = "suwyuiqwerfgqs@gmail.com"
incor_password = "12356789"

# ----------Test-Case 3----------

# register_button, wait_Registr_Account, fake_first_name, fake_last_name, email_1, fake_password, button_submit, wait_My_Account, text_My_Accound, registration_form_error in Positive Test-Case 2

gmail3 = ""
registration_error = "//span[contains(text(),'Please fill out all mandatory fields.')]"  # XPath

# ----------Test-Case 4----------

# register_button, wait_Registr_Account, fake_first_name, fake_last_name, email_1, fake_password, button_submit, wait_My_Account, text_My_Accound, registration_error in Positive Test-Case 2 and Negative Test-Case 3

gmail4 = "ypukcpa@gmail.com"
empty_password = ""
registration_error_1 = "//p[contains(text(),'Please fill out this field.')]"  # XPath


# ----------Test-Case 5----------

# logIn_button, email_const, password_const, password, button_login_submit, button_login_submit in Positive Test-Case 3

gmail_invalid = "bakyn.aliaksandr@yaho.com"
login_form_error = "//p[contains(.,'Invalid login or password. Remember that login names and passwords are case-sensitive. Please try again.')]"  # XPath

# ----------Test-Case 6----------

# logIn_button, email_const, password_const, password, button_login_submit, button_login_submit in Positive Test-Case 3 and login_form_error in Negative Test-Case 5

password_1 = "Dkps445566"

# **********Ad-hoc TESTS**********

# ----------Test-Case 1----------

# register_button, wait_Registr_Account, fake_first_name, fake_last_name, email_1, fake_password, button_submit, wait_My_Account, text_My_Accound in Positive Test-Case 2 and registration_form_error in Negative Test-Case 1

adhoc_gmail = "bakun.aliaksandr@gmail.com bakun.aliaksandr@gmail.com"
registration_error_2 = "//span[contains(text(),'Please fill out all mandatory fields.')]"  # XPath
registration_error_3 = "//p[contains(text(),'You need to have a valid email.')]"  # XPath
