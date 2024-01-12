from selenium.webdriver.common.by import By
from pages.base import *
import logging

class LoginPage(BasePage):

    username = (By.ID, 'fm-login-id')
    passward = (By.ID, 'fm-login-password')
    submit = (By.XPATH, '//*[@id="login-form"]/div[4]/button')

    # 访问到目标页面
    def to_page(self):
        self.driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.754894437.1.5af92a89SGUDCV&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
        logging.info("跳转到登录页面")

    # 输入账号数据，点击登录，返回目标值
    def act(self, data):
        self.input(self.locate(self.username), data[2])
        logging.info('输入账号{}'.format(data[2]))
        self.input(self.locate(self.passward), data[3])
        logging.info('输入密码{}'.format(data[3]))
        self.click(self.locate(self.submit))
        self.close()
        return 1