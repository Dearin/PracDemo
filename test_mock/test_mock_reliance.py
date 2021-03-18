
import requests
import unittest
from unittest import mock


class Payment:

 def requestOutofSystem(self, card_num, amount):
     '''
     请求第三方外部支付接口，并返回响应码
     :param card_num: 卡号
     :param amount: 支付金额
     :return: 返回状态码，200 代表支付成功，500 代表支付异常失败
     '''
     # 第三方支付接口请求地址(故意写错)
     url = "http://third.payment.pay/"
     # 请求参数
     data = {"card_num": card_num, "amount": amount}
     response = requests.post(url, data=data)
     # 返回状态码
     return response.status_code

 def doPay(self, user_id, card_num, amount):
     '''
     支付
     :param userId: 用户ID
     :param card_num: 卡号
     :param amount: 支付金额
     :return:
     '''
     try:
         # 调用第三方支付接口请求进行真实扣款
         resp = self.requestOutofSystem(card_num, amount)
         print('调用第三方支付接口返回结果：', resp)
     except TimeoutError:
         # 如果超时就重新调用一次
         print('重试一次')
         resp = self.requestOutofSystem(card_num, amount)

     if resp == 200:
         # 返回第三方支付成功，则进行系统里面的扣款并记录支付记录等操作
         print("{0}支付{1}成功！！！进行扣款并记录支付记录".format(user_id, amount))
         return 'success'

     elif resp == 500:
         # 返回第三方支付失败，则不进行扣款
         print("{0}支付{1}失败！！不进行扣款！！！".format(user_id, amount))
         return 'fail'

# 单元测试类
class payTest(unittest.TestCase):

 def test_pay_success(self):
     pay = Payment()
     # 模拟第三方支付接口返回200
     pay.requestOutofSystem = mock.Mock(return_value=200)
     resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
     self.assertEqual('success', resp)

 def test_pay_fail(self):
     pay = Payment()
     # 模拟第三方支付接口返回500
     pay.requestOutofSystem = mock.Mock(return_value=500)
     resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
     self.assertEqual('fail', resp)

 def test_pay_time_success(self):
     pay = Payment()
     # 模拟第三方支付接口首次支付超时,重试第二次成功
     pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 200])
     resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
     self.assertEqual('success', resp)

 def test_pay_time_fail(self):
     pay = Payment()
     # 模拟第三方支付接口首次支付超时,重试第二次失败
     pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
     resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
     self.assertEqual('fail', resp)
