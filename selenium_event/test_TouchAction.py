# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/6 18:24
@Auth ： wanghao
@File ：test_TouchAction.py
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        #add_experimental_option("w3c",False)解决错误未知命令
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        """
        打开Chrome
        打开百度
        搜索框输入'selenium测试'
        滑动到底部，点击下一页
        关闭Chrome
        """
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")
        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele,0,10000).perform()
        sleep(3)
