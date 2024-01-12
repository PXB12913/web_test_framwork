from selenium import webdriver
from settings import *

# 浏览项目首页的driver
def get_driver():
    if browser == 'Firefox':
        driver = webdriver.Firefox()
    elif browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Edge':
        driver = webdriver.Edge()
    else:
        raise Exception

    driver.get(root_url)
    return driver