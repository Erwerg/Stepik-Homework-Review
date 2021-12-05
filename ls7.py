from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

import math

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Мой ответ")

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

