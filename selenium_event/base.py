# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/11 18:31
@Auth ： wanghao
@File ：base.py
"""
import os

from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()