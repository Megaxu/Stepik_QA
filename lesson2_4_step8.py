from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import math
import pyperclip

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    price = WebDriverWait(browser, 12).until (
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    button = browser.find_element_by_id("book")
    button.click()

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
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла