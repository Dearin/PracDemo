#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/14 9:15 PM
# @Author : Deng
# @Site : 
# @File : department.py
# @Software : PyCharm
import json

import requests

from WeWorkApi.api.wework import WeWork


class Department(WeWork):
    '''
    todo:
    1、根据查询部门id
    '''
    list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
    create_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
    update_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
    delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'

    def list(self, id):
        self.json_data = requests.get(url=self.list_url, params={
            "access_token": self.get_token(), "id": id
        }).json()
        return self.json_data

    def create(self, **kwargs):
        dict_data = kwargs
        self.json_data = requests.post(
            url=self.create_url,
            params={"access_token": self.get_token()}, json=dict_data
        ).json()
        return self.json_data

    def get_departmentId_ByName(self, id, dept_name):
        '''
        根据部门名称查找部门id dept_id,存在一个问题，同一层级的部门名称不能重复，但是其他不同层级的名称是可以重复的？
        todo 优化这个方法
        :param id: 部门父级id
        :param dept_name: 被查找id的部门名称。
        :return:
        '''
        self.json_data = requests.get(url=self.list_url, params={"access_token": self.get_token(), "id": id})
        ids = self.jsonpath(expr='$..id')
        dnames = self.jsonpath(expr='$..name')
        dept_dict = dict(zip(ids, dnames))
        return dept_dict

    def update(self, **kwargs):
        dict_data = kwargs
        self.json_data = requests.post(url=self.update_url,
                                       params={"access_token": self.get_token()},
                                       json=dict_data).json()
        print(type(json))
        return self.json_data

    def delete(self, id):
        self.json_data = requests.get(url=self.delete_url, params={"access_token": self.get_token(),
                                                                   "id": id
                                                                   }).json()
        return self.json_data

    def create_and_getId(self,**kwargs):
        dict_data = kwargs
        self.json_data = requests.post(
            url=self.create_url,
            params={"access_token": self.get_token()}, json=dict_data
        ).json()
        dept_id = self.json_data['id']
        return dept_id

