#!/bin/bash/python

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方SMTP服务
mail_host="smtp.163.com"
mail_user="18861351153@163.com"
mail_pass="520224"

from_addr="18861351153@163.com"
to_addr=['18861351153@163.com','1183391310@qq.com']

msg=MIMEText('Python 邮件发送测试','plain','utf-8') #邮件正文
msg['From'] = Header("菜鸟教程", 'utf-8') #发件人名称
msg['To']= Header("一个大笨蛋", 'utf-8') #收件人名称
msg['Subject'] = Header("测试",'utf-8') #邮件主题

try:
    smtpObj = smtplib.SMTP() #构造对象
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(from_addr, to_addr, msg.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    raise

