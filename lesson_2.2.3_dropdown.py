from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Firefox()
browser.get(link)

num1 = int(browser.find_element(By.ID, "num1").text)
num2 = int(browser.find_element(By.ID, "num2").text)
answer = str(num1+num2)

# Работа с выпадающим списком
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(answer)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(20)
browser.quit()