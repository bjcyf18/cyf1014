#coding:utf-8
#执行所有用例的入口文件
import unittest
from lib.HTMLTestRunner_PY3 import  HTMLTestRunner
from config import config as cf
# from lib.send_email import send_email

# cf.receiverlogging.info("="*25+"测试开始"+"="*25)
suite=unittest.defaultTestLoader.discover(cf.testcase_path)

with open(cf.report_file,"wb") as f:
    HTMLTestRunner(stream=f,title="ApiTest",description="测试报告").run(suite)
#
# send_email(report_file)
# logging.info("邮件已发送")
#
# logging.info("="*25+"测试结束"+"="*25)