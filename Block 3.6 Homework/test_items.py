import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"), "Button is missing"
    time.sleep(30)
