from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Imya")
    browser.find_element_by_name("lastname").send_keys("Familiya")
    browser.find_element_by_name("email").send_keys("if@gmail.com")
    file_path = os.path.join('C:/Users/uigur_/Desktop', "file.txt")
    browser.find_element_by_id("file").send_keys(file_path)
    #browser.find_element_by_id("file").send_keys("C:\\Users\\uigur_\\Desktop\\file.txt")
    submit = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit.click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()