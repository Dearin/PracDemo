#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/3 2:50 PM
# @Author : Deng
# @Site : 
# @File : test_driver_remote.py
# @Software : PyCharm
from time import sleep

from selenium import webdriver



class TestTestDemo:

    def setUp_class(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_chrome(self):
        self.driver.get('https://www.baidu.com')
        sleep(5)

    # def test_wework(self):
    #     '''当前已经打开了企业微信并扫码登陆了
    #     所有可以直接访问页面元素了
    #     '''
    #     self.driver.find_element(By.ID,"menu_contacts").click()
    #     sleep(3)
