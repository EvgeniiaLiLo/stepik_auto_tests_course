from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    name.send_keys(Faker().first_name())
    last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    last_name.send_keys(Faker().last_name())
    email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    email.send_keys(Faker().email())

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()