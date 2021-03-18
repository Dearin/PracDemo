#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/3 9:23 AM
# @Author : Deng
# @Site : 
# @File : test_calc.py
# @Software : PyCharm
import pytest
import yaml


# 解析测试数据的文件
def get_datas():
    '''获取yaml测试数据'''
    # 打开文件
    with open('calc_data.yml', encoding='utf-8') as f:
        # 读取数据
        datas = yaml.safe_load(f)
        add_datas = datas['add']['datas']
        add_ids = datas['add']['ids']

    return [add_datas, add_ids]


# 解析测试步骤的文件
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if 'add' == step:
            print("step: add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step: add1")
            result = calc.add1(a, b)
        assert expect == result


class TestCalc:
    def test_add_steps(self):
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", self.calc, a, b, expect)
        # assert 2 == self.calc.add(1,1)
        # assert 3 == self.calc.add1(1,2)
        # assert 0 == self.calc.add(-1,1)

    # 使用conftest进行处理
    # def setUp_class(self):
    #     print('计算开始')
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize('a,b,expect', [[1, 2, 3], [100, 1, 200], [1, 0, 1], [-1, -1, -2]])
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = a + b
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.2, 0.3], [0.1, 0.1, 0.2]])
    def test_add_float(self, a, b, expect):
        result = a + b
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [[1, 0, 1], [1000, 100, 900], [-2, -1, -1]])
    def test_delete(self, a, b, expect):
        result = a - b
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.3, 0.2, 0.1]])
    def test_delete_float(self, a, b, expect):
        result = a - b
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, 0, 0], [10, 0, 0]])
    def test_div_zero(self, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            result = a / b
            assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[2, 4, 8], [10, 0, 0], [-1, -2, 2]])
    def test_multi(self, a, b, expect):
        result = a * b
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.2, 0.2, 0.04]])
    def test_float_multi(self, a, b, expect):
        result = a * b
        assert round(result, 2) == expect
