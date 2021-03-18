# 装饰类演示
import os
import unittest

from mock import Mock, patch


# 单独的相乘函数
def multiple(a, b):
    return a * b


# 单独的捕获Exception函数
def is_error():
    try:
        os.mkdir("11")
        return False
    except Exception as e:
        return True


# 计算类,包含add方法
class calculator(object):
    def add(self, a, b):
        return a + b


# 装饰类演示 - 单元测试类
class TestProducer(unittest.TestCase):
    '''
     @patch('module名字.方法名')
     @patch.object(类名, '方法名')
     '''

    # case执行前
    def setUp(self):
        self.calculator = calculator()
        # mock一个函数,注意也要指定module

    @patch('mock_learn.multiple')
    def test_multiple(self, mock_multiple):
        mock_multiple.return_value = 3
        self.assertEqual(multiple(8, 14), 3)

    # mock一个类对象的方法
    @patch.object(calculator, 'add')
    def test_add(self, mock_add):
        mock_add.return_value = 3
        self.assertEqual(self.calculator.add(8, 14), 3)

    # mock调用方法返回多个不同的值
    @patch.object(calculator, 'add')
    def test_effect(self, mock_add):
        mock_add.side_effect = [1, 2, 3]
        self.assertEqual(self.calculator.add(8, 14), 1)
        self.assertEqual(self.calculator.add(8, 14), 2)
        self.assertEqual(self.calculator.add(8, 14), 3)

    # mock的函数抛出Exception
    @patch('os.mkdir')
    def test_exception(self, mkdir):
        mkdir.side_effect = Exception
        self.assertEqual(is_error(), True)

    # mock多个函数,注意函数调用顺序
    @patch.object(calculator, 'add')
    @patch('mock_learn.multiple')
    def test_more(self, mock_multiple, mock_add):
        mock_add.return_value = 1
        mock_multiple.return_value = 4
        self.assertEqual(self.calculator.add(3, 3), 1)
        self.assertEqual(multiple(3, 3), 4)
