# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/12 17:09
@Auth ： wanghao
@File ：base_page.py
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    # 避免后续多次初始化driver
    def __init__(self,driver:WebDriver=None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.maximize_window()

    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def quit(self):
        return self._driver.quit()













