import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/alert_redirect.html?"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    lname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")


    fname.send_keys("Ivan")
    lname.send_keys("Petrov")
    email.send_keys("ivan.petrov@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    file = browser.find_element(By.CSS_SELECTOR, "#file")
    file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()



# не забываем оставить пустую строку в конце файла