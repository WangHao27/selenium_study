# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 11:45
@Auth ： wanghao
@File ：setting.py
"""
import csv

"""
文件路径配置
"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 日志文件存放路径
TEST_LOG = os.path.join(BASE_DIR, "logs")
# 测试数据存放路径
TEST_DATAS = os.path.join(BASE_DIR, "testdatas/addmembers_datas.csv")

def read_membbers_datas():
    with open(TEST_DATAS) as f:
        r = csv.DictReader(f)
        data = []
        for row in r:
            data.append(row)

        return data