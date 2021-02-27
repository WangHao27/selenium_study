# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/26 22:55
@Auth ： wanghao
@File ：main.py
"""
import allure
from selenium.webdriver.common.by import By
from web.page.address_book import AddressBook
from web.page.base_page import BasePage


class Main(BasePage):

    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 点击添加成员，跳转通讯录
    @allure.story("首页跳转至通讯录")
    def goto_addressBook(self):
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "div.index_service_cnt.js_service_list>a:nth-child(1)").click()
        return AddressBook()
