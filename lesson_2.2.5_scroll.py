from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# чтобы кликнуть на перекрытую кнопку, нужно прокрутить страницу вниз
# с поомощью JavaScript
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)
browser.quit()

# Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. 
# Эта команда проскроллит страницу на 100 пикселей вниз:
# browser.execute_script("window.scrollBy(0, 100);")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) --- прокручивает вниз
# browser.execute_script("return arguments[0].scrollIntoView(false);", button) --- прокручивает вверх

# browser.execute_script("arguments[0].scrollIntoView({block: 'nearest', inline: 'center'});", expand_button)
# прокручивает элемент в центр экрана по горизонтали, а по вертикали - к ближайшему краю
# block: 'nearest' → minimal vertical scroll
# inline: 'center' → horizontal scroll to center the element