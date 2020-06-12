from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome("D:\Courses\drivers\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_FN = browser.find_element_by_css_selector(".first_block input.form-control.first")
    input_LN = browser.find_element_by_css_selector(".first_block input.form-control.second")
    input_email = browser.find_element_by_css_selector("input.form-control.third")
    input_FN.send_keys("nfdsa")
    input_LN.send_keys("fuafias")
    input_email.send_keys("fbafashbfas")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
