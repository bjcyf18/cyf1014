#coding:utf-8

import logging
import os

#项目路径
prj_path= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))
print(prj_path)
# 数据文件路径
data_path=os.path.join(prj_path,'data')
# data_file = os.path.join(prj_path,'data','data.xlsx')
#测试用例路径
testcase_path = os.path.join(prj_path,'testcase')
print(testcase_path)
#报告路径
report_file = os.path.join(prj_path,'report','report.html')
print(report_file)

#日志文件路径
log_file=os.path.join(prj_path,'log','log.txt')

#全局log配置
logging.basicConfig(level=logging.INFO, # 日志级别
                   format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                   datefmt="%Y-%m-%d %H:%M:%S", #日期格式
                   filename=log_file, #日志输出文件
                   filemode="a")  #追加模式

#数据库配置
db_host='115.28.108.130'
db_port=3306
db_user='test'
db_password='123456'
db='api_test'
#邮件配置

smtp_server='stmp.163.com'  #smtp 服务器地址
smtp_user='ivan-me@163.com'
smtp_password='hanzhichao123'

sender=smtp_user #邮件发送人
receiver='2210562954@qq.com' #邮件接收人
subject='接口测试报告'  #邮件主题

is_send_email=False #是否发送邮件开关

email_body='hi,all\n测试完成，请查看附件'

if __name__ == '__main__':
    # logging.debug('helloworld')
    print(report_file)
