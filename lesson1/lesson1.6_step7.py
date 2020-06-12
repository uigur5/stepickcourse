from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome("D:\Courses\drivers\chromedriver.exe")
    browser.get(link)

    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
