from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def link_t(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        
        input1 = browser.find_element(By.CSS_SELECTOR, value=".first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, value=".first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, value=".first_block input.third")
        input3.send_keys("mops@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, value="h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        return welcome_text_elt.text

    except:
        browser.quit()

def test_registration1():
    congratulation_test = "Congratulations! You have successfully registered!"
    welcome_text = link_t("http://suninjuly.github.io/registration1.html")
    assert welcome_text == congratulation_test, "Registration1 fall"
        
def test_registration2():
    congratulation_test = "Congratulations! You have successfully registered!"
    welcome_text = link_t("http://suninjuly.github.io/registration2.html")
    assert welcome_text == congratulation_test, "Registration2 fall"
        
if __name__ == "__main__":
    pytest.main()