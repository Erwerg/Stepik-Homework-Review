def test_ls8_1():

        from selenium import webdriver
        import time

        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")

            input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
            input3.send_keys("test@test.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

        assert "Congratulations! You have successfully registered!" ==  welcome_text, "Text is not equal"

def test_ls8_2():

        from selenium import webdriver
        import time

        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration2.html")

            input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
            input3.send_keys("test@test.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

        assert "Congratulations! You have successfully registered!" ==  welcome_text, "Text is not equal"
