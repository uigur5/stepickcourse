from selenium import webdriver
import unittest
import time
import math
import pytest


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236905", "236905"])
# @pytest.mark.parametrize('number', ["236895", "236896"])
def test_parametrize(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('.textarea').send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission ").click()
    time.sleep(10)
    assert browser.find_element_by_class_name("smart-hints__hint").text == "Correct!"
