'''
NoSuchElementException
Если элемент не был найден за отведенное время

StaleElementReferenceException
Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился.
Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный 
нам метод click. Если кнопка за это время была скрыта скриптом, 
то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.

ElementNotVisibleException
Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), 
и реальный пользователь не смог бы с ним взаимодействовать.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/cats.html")
    button = browser.find_element(By.ID, "button")
    button.click()
finally:
    browser.quit()