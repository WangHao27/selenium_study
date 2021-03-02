# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/26 22:55
@Auth ： wanghao
@File ：base_page.py
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.utils.log import Log

# 导入日志类
log = Log()
class BasePage:
    base_url = ""
    # 避免后续多次初始化driver
    # driver:WebDriver类型提示
    def __init__(self, driver: WebDriver = None):
        self.driver = ""
        if driver is None:
            # 复用已经打开的浏览器
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver
        # 全局设置隐式等待
        self.driver.implicitly_wait(5)
        if self.base_url != "":
            self.driver.get(self.base_url)
        self.driver.maximize_window()

    # 查找单个元素
    def find(self, *locator):
        try:
            # 等待某个元素可见
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            log.info(f'页面未找到{locator}元素')
            raise e

    # 查找多个元素
    def finds(self, *locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
            return self.driver.find_elements(*locator)
        except NoSuchElementException as e:
            log.info(f'页面未找到{locator}元素')
            raise e

    # 显示等待某个元素可点击，并执行点击操作
    def wait_for_click(self, timeout, locator):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except NoSuchElementException as e:
            log.info(f'该元素{locator}不可点击')
            raise e

    # 退出浏览器
    def quit(self):
        return self.driver.quit()