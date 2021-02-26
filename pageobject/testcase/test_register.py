# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/12 17:38
@Auth ： wanghao
@File ：test_register.py
"""
from time import sleep

from pageobject.page.base_page import BasePage
from pageobject.page.main import Main

class TestRegister():
    def setup(self):
        self.main = Main()

    def teardown(self):
        self.base = BasePage()
        self.base.quit()


    def test_register(self):
        assert  self.main.goto_register().register()
