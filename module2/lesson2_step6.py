from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    submit = browser.find_element_by_css_selector("button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
