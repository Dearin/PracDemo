#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/3 11:26 AM
# @Author : Deng
# @Site : 
# @File : calc.py
# @Software : PyCharm

class Calculator:
    '''被测函数'''
    def add(self, a, b):
        return a + b

    def add1(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b
