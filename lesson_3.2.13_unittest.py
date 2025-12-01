from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
import unittest

class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Firefox()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        name.send_keys(Faker().first_name())
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        last_name.send_keys(Faker().last_name())
        email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        email.send_keys(Faker().email())
        time.sleep(3)

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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()