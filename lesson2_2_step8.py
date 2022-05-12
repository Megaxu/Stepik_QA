from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Mops")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Mops")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("Mops")


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)

    input_file = browser.find_element_by_name("file")
    input_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла