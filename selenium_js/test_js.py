# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/11 18:47
@Auth ： wanghao
@File ：test_js.py
"""
from time import sleep
from selenium_js.base import Base


class TestJs(Base):

    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys("selenium测试")
        sleep(2)
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(1)
        # for code in { # 获取标题；获取页面性能数据
        #     'return document.title','return JSON.stringify(performance.timing)'
        # }:
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-02-12'")
        sleep(1)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))


















