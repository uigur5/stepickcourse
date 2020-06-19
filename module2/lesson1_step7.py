from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn.btn-default").click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
