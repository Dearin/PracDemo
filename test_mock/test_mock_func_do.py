import unittest

from mock import Mock


class SubClass(object):
    '''被测对应方法已经完成开发'''

    def add(self, a, b):
        return a + b


class TestSubClass(unittest.TestCase):
    def test_subadd(self):
        sub = SubClass()
        sub.add = Mock(return_value=10, side_effect=sub.add)
        # side_effect 可以覆盖return_value设置的参数
        self.assertEqual(sub.add(4, 3), 7)
