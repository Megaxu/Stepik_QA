from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)

    result = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(result)

    checkBox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkBox)
    checkBox.click()

    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()

    button = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла