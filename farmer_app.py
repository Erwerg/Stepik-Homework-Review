from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting the browser options for mobile emulation
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=en")

# Setting entry testing data
uber_test_email = "shasth+test+farmers+mich+detroit+deductible+uberx+test4@ext.uber.com"
uber_test_password = "uber1234"
customer_first_name = "Arkadiy"
customer_last_name = "Kvasin"
customer_address = "100 Michigan Avenue, Detroit, MI, USA"
customer_address_apt = "123"
customer_address_update = "200 Michigan Avenue, Detroit, MI, USA"
customer_address_apt_update = "456"
customer_email = "deductible.buydown+testarkadiy01@gmail.com"
customer_email_update = "deductible.buydown+test_ar@gmail.com"
customer_phone = "2752398682"
customer_phone_update = "2752398683"
customer_dl_number = "P800900700333"
customer_vehicle_number = "WVW35ANCA01130004"
customer_auto_number = "US-FARMERS-TQ004"   # I forgot what this number is
customer_card_holder = "{} {}".format(customer_first_name, customer_last_name)

uber_sign_in_link = "https://auth.uber.com/login/"
uber_insurance_hub_link = "https://driverinjuryprotection.uber.com/insurance-hub/"
sure_app_policy_overview_link = "https://www.tryfarmersdeductiblebuydown.com/policy/2804b516-33d1-4ec1-a1fc-4a5d345c5030/overview"

try:
    # Driver initialization
    browser = webdriver.Chrome(options=chrome_options)
    # WebDriver must search for each element within 10 seconds
    browser.implicitly_wait(10)

    # Uber sign-in
    browser.get(uber_insurance_hub_link)
    browser.find_element_by_id('useridInput').send_keys(uber_test_email)
    browser.find_element_by_css_selector("button.btn").click()
    browser.find_element_by_id('password').send_keys(uber_test_password)
    browser.find_element_by_css_selector("button.btn").click()

    # Go to insurance-hub (if the automatic redirection to insurance-hub does not work)
    # browser.get(uber_insurance_hub_link)
    browser.find_element_by_xpath('//*[contains(., "Optional Lower Physical Damage Deductible")]').click()

    # Customer address update
    browser.find_element_by_xpath('//button[@data-testid="policyHolder_editPolicyDetailsBtn"]').click()
    browser.find_element_by_xpath('//input[@data-testid="inputAddressAutocomplete_streetAddress"]').send_keys(customer_address_update)
    browser.find_element_by_xpath('//input[@data-testid="input_addressLine2"]').send_keys(customer_address_apt_update)

    browser.find_element_by_xpath('//input[@data-testid="inputAddressAutocomplete_streetAddress"]').click()
    browser.find_element_by_xpath('//input[@data-testid="input_addressLine2"]').click()
    hide_button = browser.find_element_by_xpath('//button[@data-testid="ModalEditPolicyAddress_save_button"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", hide_button)
    hide_button.click()

    #element = browser.find_element_by_tag_name('body')
    browser.save_screenshot(r"C:\Users\kirpa\environments\test_farmers.png")
    #element.screenshot(r"C:\Users\kirpa\environments\test_full.png")


    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()


finally:
    # delay to check test results
    time.sleep(10)
    # browser closing
    browser.quit()
