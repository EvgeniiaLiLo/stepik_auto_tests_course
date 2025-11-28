from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Firefox()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    current_window = browser.current_window_handle

    browser.switch_to.window(new_window)


finally:
    time.sleep(10)
    browser.quit()