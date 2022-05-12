from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import pyperclip

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    alert = browser.switch_to.alert.accept()

    x = int(browser.find_element_by_id("input_value").text)

    result = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(result)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    alert = browser.switch_to.alert
    text = alert.text.split(': ')[-1]
    pyperclip.copy(text)
    alert.accept()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла