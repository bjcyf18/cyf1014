#coding:utf-8

import unittest
import requests
import json
# from config.config import  *
# from lib.read_excel import get_data
# import os
import sys
sys.path.append("..")
from config import config as cf
from lib.read_excel import get_case_data


class TestUserLogin(unittest.TestCase):
    def test_user_login_normal(self):

        # 用例数据
        # url="http://115.28.108.130:5000/api/user/login/"
        # date={"name":"张三","password":"123456"}
        # expect_res = '<h1>登录成功</h1>'
        case_data = get_case_data('data.xlsx', 'TestUserLogin', 'test_01')
        url = case_data[1]
        # data_dirt = json.loads(case_data)  # json 格式的字符串 -》 字典
        data=case_data[3]  #需要转换为字典

        expect_res = case_data[4]

        data_dirt=json.loads(data)
        cf.logging.info("测试用例：{}".format("test_user_login_normal"))
        cf.logging.info("url: {}".format(url))
        cf.logging.info("请求数据：{}".format(data))
        cf.logging.info("期望结果：{}".format(expect_res))

        #发送请求
        req=requests.post(url=url,data=data_dirt)

        self.assertEqual(req.text, expect_res)



    # def test_user_login_password_wrong(self):
    #     url = "http://115.28.108.130:5000/api/user/login/"
    #     data = {"name": "张三", "password": "12345"}
    #     expect_res = '<h1>失败，用户名或密码错误</h1>'
    #     req = requests.post(url=url, data=data)   #data支持文本or字典
    #     # assert req["code"] == 200
    #     self.assertEqual(req.text, expect_res)

if __name__=='_main__':
    t=TestUserLogin()
    t.test_user_login_normal()
    t.test_user_login_password_wrong()