from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = int(x_element.text)
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(20)
browser.quit()
