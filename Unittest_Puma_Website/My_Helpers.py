# ----------Website address----------

url = "https://us.puma.com/us/en"

# **********POSITIVE TESTS**********

# ----------All Test-Cases and Test-Case 1----------

menu_bar = "//ul[contains(@role,'menubar')]"  # XPath
popUp_message_1 = "//button[contains(@data-test-id,'stay-on-region-button')]"  # Location
popUp_message_2 = "(//div[contains(@data-uds-child,'action-icon-icon')])[1]"  # Website uses Cookies
account_button = "account-button"  # ID

# ----------Test-Case 2----------

# Registration User Account:

register_button = "//a[contains(@data-test-id,'register-button')]"  # XPath
wait_Registr_Account = "//p[contains(.,'My account')]"  # XPath
fake_first_name = "firstName"  # NAME
fake_last_name = "lastName"  # NAME
email_1 = "email"  # NAME
# You need to change email every time you test
gmail = "tpbmht@gmail.com"
gmail_firefox = "hgyrhawj@gmail.com"
gmail_edge = "uitoorje@gmail.com"
gmail_safari = "nvbysyrh@gmail.com"
fake_password = "password"  # NAME
button_submit = "//button[@type='submit']"  # XPath
wait_My_Account = "(//div[contains(@data-uds-child,'stack')])[2]"  # XPath
text_My_Accound = "//span[contains(text(),'My account')]"  # XPath

# ----------Test-Case 3----------

logIn_button = "//a[@data-test-id='login-button']"  # XPath
email_const = "email"  # ID
gmail_const = "Bialenik.Aliaksandr@gmail.com"
password_const = "password"  # ID
password = "Bialenik1234"
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
postal_code = 10005
state = "//option[contains(text(),'New York')]"  # XPath
phone_input = "phone-input"  # ID
phone_number = "+14845524458"
button_default_address = "preferred-address"  # ID
button_submit_contains = "//button[contains(@type,'submit')]"  # XPath
wait_Dashboard = "//p[@class='tw-1xl28s9 tw-1p4ksvz'][contains(.,'My accountDashboard')]"
wait_menu_address = "//address[contains(@data-test-id,'address-information')]"  # XPath

# ----------Test-Case 5----------

# logIn_button, email_const, gmail_const, password_const, password, button_login_submit, logOut_button in Test-Case 3
# wait_new_address, address_title_input, address1, postalCode, button_submit_contains, wait_menu_address  in Test-Case 4

button_edit_address = "//a[contains(@data-test-id,'edit-address')]"  # XPath
address_title_new = "Broadway, New York"
address_new = "1567 Broadway, New York"
postal_code_new = 10036
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
gmail2 = "uukhka@gmail.com"
gmail_firefox2 = "urhsbcfl@gmail.com"
gmail_edge2 = "nbbshsu@gmail.com"
gmail_safari2 = "lnsgqsb@gmail.com"
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

gmail_invalid = "Bialenik.Aliaksandr@mail.com"
login_form_error = "//p[contains(.,'Invalid login or password. Remember that login names and passwords are case-sensitive. Please try again.')]"  # XPath

# ----------Test-Case 6----------

# logIn_button, email_const, password_const, password, button_login_submit, button_login_submit in Positive Test-Case 3 and login_form_error in Negative Test-Case 5

password_1 = "Dkps445566"

# **********Ad-hoc TESTS**********

# ----------Test-Case 1----------

# register_button, wait_Registr_Account, fake_first_name, fake_last_name, email_1, fake_password, button_submit, wait_My_Account, text_My_Accound in Positive Test-Case 2 and registration_form_error in Negative Test-Case 1

adhoc_gmail = "Bialenik.Aliaksandr@gmail.com Bialenik.Aliaksandr@gmail.com"
registration_error_2 = "//span[contains(text(),'Please fill out all mandatory fields.')]"  # XPath
registration_error_3 = "//p[contains(text(),'You need to have a valid email.')]"  # XPath
