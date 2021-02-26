# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/7 23:06
@Auth ： wanghao
@File ：test_frame.py
"""
from selenium import webdriver

from selenium_event.base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN")