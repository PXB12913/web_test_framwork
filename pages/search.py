import logging

from selenium.webdriver.common.by import By

from pages.base import *

class SearchPage(BasePage):

    input_text = (By.ID, 'q')
    search_btn = (By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')

    # 访问目标页面
    def to_page(self):
        pass

    # 输出搜索词，点击搜索，返回目标值
    def act(self, data):
        self.input(self.locate(self.input_text), data[2])
        logging.info('输入搜索词{}'.format(data[2]))
        self.click(self.locate(self.search_btn))
        self.close()
        return 1