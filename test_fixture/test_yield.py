#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/2 11:28 PM
# @Author : Deng
# @Site : 
# @File : test_yield.py
# @Software : PyCharm

# 方法会默认使用conn_db这个装饰器
class TestFixture:
    def test_case1(self, login):
        print(login)
        print("用例1")

    def test_case2(self):
        print("用例2")

    def test_case3(self, conn_db):
        print(conn_db)
        print("用例3")
