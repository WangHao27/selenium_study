# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/11 21:08
@Auth ： wanghao
@File ：test_alert.py
"""
from time import sleep
from selenium.webdriver import ActionChains
from selenium_event.base import Base


class TestAlert(Base):
    def test_alert(self):
        """
        打开网页 https : / / www.runoob.com/try/try.php?filename=jqueryui-api-droppable操作窗口右侧页面，将元素1拖拽到元素2
        这时候会有一个alert弹框，点击弹框中的'确定′然后再按'点击运行′
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(2)
        # 点击alert确认按钮
        self.driver.switch_to.alert.accept()
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(2)