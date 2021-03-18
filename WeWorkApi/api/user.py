#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/17 5:32 PM
# @Author : Deng
# @Site : 
# @File : user.py
# @Software : PyCharm
import requests

from WeWorkApi.api.wework import WeWork


class User(WeWork):
    create_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'

    def create(self, **kwargs):
        dict_data = kwargs
        self.json_data = requests.post(url=self.create_url, params={
            "access_token": self.get_token()
        }, json=dict_data).json()
        return self.json_data
