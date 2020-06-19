from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    num1 = int(x)
    num2 = int(y)
    sum = num1 + num2
    sum = str(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    browser.find_element_by_css_selector("button.btn.btn-default").click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
