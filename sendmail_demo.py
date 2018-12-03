#!/bin/bash/python
from email.mime.text import MIMEText #构造邮件模块
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib #发送邮件模块

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'xxx@163.com'
password = 'xxx'
to_addr = 'xxx@qq.com,xxx@163.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello,send by Python...', 'plain', 'utf-8') #邮件正文,纯文本,utf-8编码
msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
msg['To'] = to_addr
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr.split(','), msg.as_string())
server.quit()

