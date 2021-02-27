# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 0:08
@Auth ： wanghao
@File ：address_book.py
"""
from time import sleep

import allure
from selenium.webdriver.common.by import By

from web.page.base_page import BasePage


class AddressBook(BasePage):

    # 添加成员
    @allure.story("添加成员")
    def add_members(self, username, acctId, phoneNum):
        # 成员姓名
        self.find(By.ID, "username").send_keys(username)
        # 成员账号
        self.find(By.ID, "memberAdd_acctid").send_keys(acctId)
        # 手机号
        self.find(By.ID, "memberAdd_phone").send_keys(phoneNum)
        # 保存
        self.find(By.CSS_SELECTOR, "div.member_colRight_operationBar.ww_operationBar>a:nth-child(2)").click()
        sleep(1)
        return username

    # 获取所有分页成员名单
    @allure.story("获取所有分页成员名单")
    def check_members(self):
        self.find(By.CSS_SELECTOR, "div.member_colRight_operationBar.ww_operationBar>a:nth-child(3)").click()

        # 获取页码文本，并转为int页数
        str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
        pageNum = int(str.split('/')[1])

        name_list = []
        # 根据页数循环获取成员元素并追加
        for num in range(pageNum):
            elements = self.finds(By.CSS_SELECTOR,
                                      "tr.member_colRight_memberTable_tr.member_colRight_memberTable_tr_Inactive>td:nth-child(2)")
            # 循环获取当前页面成员姓名
            for ele in elements:
                name = ele.get_attribute('title')
                name_list.append(name)
            # 点击下一页
            self.find(By.CSS_SELECTOR, ".ww_pageNav_info_arrowWrap.js_next_page").click()
        return name_list
