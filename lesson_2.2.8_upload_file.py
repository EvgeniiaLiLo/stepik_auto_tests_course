from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from faker import Faker

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

first_name = browser.find_element(By.NAME, "firstname")
first_name.send_keys(Faker().first_name())
last_name = browser.find_element(By.NAME, "lastname")
last_name.send_keys(Faker().last_name())
email = browser.find_element(By.NAME, "email")
email.send_keys(Faker().email())

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
upload_file = browser.find_element(By.ID, "file")
upload_file.send_keys(file_path)

submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()
time.sleep(20)
browser.quit()
