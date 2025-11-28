from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from faker import Faker

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

alert = browser.switch_to.alert
alert.accept()
alert_text = alert.text

confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

# prompt — имеет дополнительное поле для ввода текста
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()