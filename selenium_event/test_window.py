# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/7 22:35
@Auth ： wanghao
@File ：test_window.py
"""
from time import sleep

from selenium import webdriver


class TestWindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
       self.driver.quit()

    #百度注册
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        #获取所有窗口句柄
        new_win = self.driver.window_handles
        #切换至注册页面
        self.driver.switch_to_window(new_win[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        sleep(3)
        #切回百度首页
        self.driver.switch_to_window(new_win[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("wanghao")