import unittest
from unittest import mock


def add(self, a, b):
    # 功能暂未完成
    pass


class TestMock(unittest.TestCase):
    '''功能未完成，mock一个方法'''

    def test_add(self):
        # 当测试的功能未开发时，实例化一个mock对象并赋值给被测方法
        mock_add = mock.Mock(return_value=6)
        add = mock_add
        self.assertEqual(add(3, 3), 6)



