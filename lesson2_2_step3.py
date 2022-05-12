from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects2.html"

def sum(x, y):
    return x + y

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = browser.find_element_by_id("num1")
    second_number = browser.find_element_by_id("num2")
    
    x = int(first_number.text)
    y = int(second_number.text)

    result = str(sum(x, y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)    

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла