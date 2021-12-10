import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# this var will be global
total_result = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
    # print total result of all tests
    print(total_result)

@pytest.mark.parametrize('lesson', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_math_check(browser, lesson):
    # declaire of global var
    global total_result

    browser.get(f'https://stepik.org/lesson/{lesson}/step/1')
    input = browser.find_element_by_tag_name("textarea")
    answer = str(math.log(int(time.time())))
    input.send_keys(answer)

    WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
    test_result = browser.find_element_by_class_name("smart-hints__hint").text

    try:
        assert "Correct!" == test_result, "The result is incorrect!"

    except AssertionError:
        total_result += test_result
