# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/6 19:56
@Auth ： wanghao
@File ：test_form.py
"""
from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        #元素无法点击，使用js脚本
        ele = self.driver.find_element_by_id("user_remember_me")
        self.driver.execute_script("arguments[0].click();", ele)
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[4]/input")
        sleep(3)