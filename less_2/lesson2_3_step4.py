import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    but = browser.find_element(By.CSS_SELECTOR, ".btn")
    but.click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x.text))
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()



# не забываем оставить пустую строку в конце файла