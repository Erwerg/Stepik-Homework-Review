from selenium import webdriver
import time

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

try:
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://driverinjuryprotection.uber.com/insurance-hub")

    element = browser.find_element_by_tag_name('body')
    browser.save_screenshot(r"C:\Users\kirpa\environments\test.png")
    element.screenshot(r"C:\Users\kirpa\environments\test_full.png")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
