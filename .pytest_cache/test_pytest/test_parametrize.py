#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/2 4:33 PM
# @Author : Deng
# @Site : 
# @File : test_parametrize.py
# @Software : PyCharm
import pytest


class TestParam:
    @pytest.mark.parametrize('a', [1, 2, 3, 4, 5])
    def test_add(self, a: int):
        assert a == 4
