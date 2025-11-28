from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Firefox()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
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
