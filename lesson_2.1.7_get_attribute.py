from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Firefox()
browser.get(link)

#Найдём атрибут "treasure" с помощью встроенного метода get_attribute и проверим его значение
x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(20)
browser.quit()
