#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/14 8:58 PM
# @Author : Deng
# @Site : 
# @File : utils.py
# @Software : PyCharm
from jsonpath import jsonpath


class Utils:
    ''' 存放对其他功能的封装，改进原生框架 '''

    @classmethod
    def jsonpath(cls, json_object, expr):
        '''取json体中的数据'''
        return jsonpath(json_object, expr)
