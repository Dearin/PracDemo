#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/14 9:01 PM
# @Author : Deng
# @Site : 
# @File : wework.py
# @Software : PyCharm
import requests

from WeWorkApi.api.base_api import BaseApi


class WeWork(BaseApi):
    '''实现一些通用的方法'''
    corp_id = 'ww527f8b180913ddef'
    contact_secret = 'LdUgTbiD3KNk-pMLeByM-5nRglOOslMtxCcbjNNeTlY'
    token = dict()
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'

    @classmethod
    def get_token(cls, secret=contact_secret):
        # 避免重复请求，提高速度
        # 若token中没有对应存入响应的token值，则请求一次接口并保存数据
        if secret not in cls.token.keys():
            result = cls.get_access_token(secret)
            cls.token[secret] = result['access_token']
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        res = requests.get(url=cls.token_url, params={'corpid': cls.corp_id, 'corpsecret': cls.contact_secret})
        return res.json()
