from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("solve").click()
finally:
    time.sleep(10)
    browser.quit()
