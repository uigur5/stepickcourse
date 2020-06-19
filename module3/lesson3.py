from selenium import webdriver
import unittest
import time

class lesson3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.link1 = "http://suninjuly.github.io/registration1.html"
        cls.link2 = "http://suninjuly.github.io/registration2.html"
        cls.browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")

        # Ваш код, который заполняет обязательные поля
    def test_register1(self):
        self.browser.get(self.link1)
        self.browser.find_element_by_xpath("//div[1]/div[1]/input[@placeholder = 'Input your first name']").send_keys("first")
        self.browser.find_element_by_class_name("form-control.second").send_keys("last")
        self.browser.find_element_by_class_name("form-control.third").send_keys("email")
        self.browser.find_element_by_css_selector("div.second_block>div.form-group.first_class>input").send_keys("0933333333")
        self.browser.find_element_by_css_selector("div.second_block>div.form-group.second_class>input").send_keys("address")
        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_register2(self):
        self.browser.get(self.link2)
        self.browser.find_element_by_xpath("//div[1]/div[1]/input[@placeholder = 'Input your first name']").send_keys("first")
        self.browser.find_element_by_class_name("form-control.second").send_keys("last")
        self.browser.find_element_by_class_name("form-control.third").send_keys("email")
        self.browser.find_element_by_css_selector("div.second_block>div.form-group.first_class>input").send_keys("0933333333")
        self.browser.find_element_by_css_selector("div.second_block>div.form-group.second_class>input").send_keys("address")
        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    @classmethod
    def tearDownClass(cls):
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        cls.browser.quit()


if __name__ == "__main__":
    unittest.main()
