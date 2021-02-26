# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/11 20:51
@Auth ： wanghao
@File ：test_file.py
"""
from time import sleep
from selenium_event.base import Base


class TestFile(Base):

    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_class_name("st_camera_off").click()
        self.driver.find_element_by_id("stfile").send_keys("E:/元气壁纸缓存/img/3a7b57693d63b7b89ce1cd6ad5333125.jpg")
        sleep(5)


