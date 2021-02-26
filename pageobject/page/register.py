# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/12 17:26
@Auth ： wanghao
@File ：register.py
"""

from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("企业名称")
        self.find(By.ID,"manager_name").send_keys("管理人员")
        return True