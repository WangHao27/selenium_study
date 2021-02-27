# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 0:14
@Auth ： wanghao
@File ：test_addmembers.py
"""
import pytest
from web.page.main import Main
from web.utils import setting

membbers_datas = setting.read_membbers_datas()
class TestAddMembers:

    def setup(self):
        self.main = Main()


    def teardown(self):
        # self.main.quit()
        pass

    # 添加通讯录人员名单
    @pytest.mark.parametrize('params', membbers_datas)
    def test_addmembers(self,params):
        add_menmber = self.main.goto_addressBook().add_members(params['username'], params['acctId'], params['phoneNum'])
        all_members = self.main.goto_addressBook().check_members()
        assert add_menmber in all_members
