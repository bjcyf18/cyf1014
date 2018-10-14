#coding:utf-8

import  smtplib
from email.mime.text   import MIMEText #邮件正文
from email.mime.multipart import  MIMEMultipart  #用来上传附件

import sys
sys.path.append("..") #提升包搜索路径到项目路径
from config import config as cf
def send_report():
    msg=MIMEMultipart() #混合格式的邮件
    #邮件正文

    body=MIMEText('测试报告','plain','utf-8') #plain 是普通文本，也可以是html
    msg.attach(body)
    #邮件头
    msg['From'] =cf.sender
    msg['To'] =cf.receiver
    msg['Subject']=cf.subject
    #报告附件
    with open(cf.report_file,'rb') as f:
        att_file=f.read()
    att1=MIMEText(att_file,'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)

    #发送邮件
    smtp = smtplib.SMTP_SSL(cf.smtp_server)
    smtp.login(cf.smtp_user, cf.smtp_password)
    smtp.send(cf.sender, cf.receiver, msg.as_string())
    cf.logging.info("send email done")

if __name__=="__main__":
    send_report()




#1.编写email正文 MIME格式

# msg =MIMEText('helloworld','plain','utf-8')
# msg=MIMEText('<h1>这是一封测试邮件</h1>','plain','utf-8')
# #2.编写email头
# msg['From'] ="test_results@sina.com"
# msg['to'] ='2210562954@qq.com'
# msg['Subject'] ="Test"
# #链接smtp服务器，发送邮件
# # smtp = smtplib.SMTP_SSL("stmp.sina.com")
# smtp=smtplib.SMTP_SSL("smtp.sina.com")
#
# smtp.login("test_results@sina.com","hanzhichao123")
# smtp.sendmail("test_results@sina.com",'2210562954@qq.com',msg.as_string())
# smtp.quit()
#
# print("发送完成")

# # 1. 编写email正文 MIME
# msg = MIMEText('<h1>这是一封Python发送的邮件</h1><h2>hello</h2>','html','utf-8')
# # 2. 编写email头
# msg['From'] = "ivan-me@163.com"
# msg["To"] = 'superhin@126.com'
# msg['Subject'] = "中文"
# # 3. 连接smtp服务器，发送邮件
# smtp = smtplib.SMTP("smtp.163.com")
# smtp.login("ivan-me@163.com","hanzhichao123")
# # smtp.sendmail("test_results@sina.com",'superhin@foxmail.com',msg.as_string())
# smtp.sendmail("ivan-me@163.com",'superhin@126.com',msg.as_string())
# smtp.quit()
# print("发送完成")


# msg=MIMEMultipart()
# msg.attach(MIMEText("hi,all\n测试完成请查看附件",'plain','utf-8'))
# msg['From'] = "ivan-me@163.com"
# msg["To"] = '2210562954@qq.com'
# msg['Subject'] = "接口测试报告"
# with open("report1.html",'rb') as f:
#     att1_body=f.read()
#
# att1=MIMEText(att1_body,'base64','utf-8')  #base64：文件流输出格式
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="report.html"' #附件名字
#
# msg.attach(att1)
#
# smtp = smtplib.SMTP("smtp.163.com")
# smtp.login("ivan-me@163.com","hanzhichao123")
# smtp.sendmail("ivan-me@163.com",'2210562954@qq.com',msg.as_string())
# smtp.quit()
# print("发送完成")

# def send_email(report_file):
#     msg = MIMEMultipart()
#     msg.attach(MIMEText("hi,all\n测试完成请查看附件", 'plain', 'utf-8'))
#     msg['From'] = "ivan-me@163.com"
#     msg["To"] = '2210562954@qq.com'
#     msg['Subject'] = "接口测试报告"
#     with open(report_file, 'rb') as f:
#         att1_body = f.read()
#
#     att1 = MIMEText(att1_body, 'base64', 'utf-8')  # base64：文件流输出格式
#     att1["Content-Type"] = 'application/octet-stream'
#     att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)  # 附件名字
#
#     msg.attach(att1)
#
#     smtp = smtplib.SMTP("smtp.163.com")
#     smtp.login("ivan-me@163.com", "hanzhichao123")
#     smtp.sendmail("ivan-me@163.com", '2210562954@qq.com', msg.as_string())
#     smtp.quit()

# def send_email(report_file):
#     msg = MIMEMultipart()
#     msg.attach(MIMEText("hi,all\n测试完成请查看附件", 'plain', 'utf-8'))
#     msg['From'] =sender
#     msg["To"] = receiver
#     msg['Subject'] = subject
#     with open(report_file, 'rb') as f:
#         att1_body = f.read()
#
#     att1 = MIMEText(att1_body, 'base64', 'utf-8')  # base64：文件流输出格式
#     att1["Content-Type"] = 'application/octet-stream'
#     att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)  # 附件名字
#
#     msg.attach(att1)
#
#     smtp = smtplib.SMTP(smtp_server)
#     smtp.login(smtp_user, smtp_password)
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()

