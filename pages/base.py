from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from utils.driver import *
import allure

class BasePage:

    # 设置浏览器驱动
    def __init__(self):
        self.driver = get_driver()
        self.wait = WebDriverWait(self.driver, 1)

    # 定位
    def locate(self, params):
        return self.wait.until(
            visibility_of_element_located(params)
        )

    # 点击
    def click(self, element):
        element.click()

    # 输入
    def input(self, element, data, type='input'):
        element.send_keys(data)

    # # 截图
    # def screenshot(self):
    #     allure.attach(self.driver.get_screenshot_as_file(""))

    # 关闭
    def close(self):
        self.driver.close()