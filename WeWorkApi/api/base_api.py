#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/14 9:01 PM
# @Author : Deng
# @Site : 
# @File : base_api.py
# @Software : PyCharm

from WeWorkApi.utils.utils import Utils


class BaseApi:
    ''' 在此文件中调用utils的jsonpath方法 '''
    json_data = None

    def jsonpath(self, expr):
        return Utils.jsonpath(self.json_data, expr)
