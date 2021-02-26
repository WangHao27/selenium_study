# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/6 16:37
@Auth ： wanghao
@File ：test_ActionChains.py
"""
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    #元素点击，双击，右击
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        ele_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        ele_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_rightclick)
        action.double_click(ele_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    #移动光标至某个元素
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        #设置按钮
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    #拖拽元素到某处
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        drop_ele = self.driver.find_element_by_xpath("/html/body/div[4]")
        action = ActionChains(self.driver)
        #方法一,拖拽元素到目标位置
        # action.drag_and_drop(drag_ele,drop_ele)
        #方法二,点击元素按住到目标位置释放
        # action.click_and_hold(drag_ele).release(drop_ele)
        #方法三，点击元素按住，移动到目标位置后释放
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release()
        action.perform()
        sleep(3)

    #模拟键盘操作
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input").click()
        #pause等待操作
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("wanghao").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)