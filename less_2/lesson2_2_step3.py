
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    val1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    val2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))

    select.select_by_value(str(int(val1.text) + int(val2.text)))


    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()



# не забываем оставить пустую строку в конце файла