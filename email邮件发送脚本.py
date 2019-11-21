#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-

import smtplib,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

yesterday = datetime.date.today() - datetime.timedelta(days=1)  #昨天的日期
days = str(datetime.date.strftime(yesterday, '%Y%m%d'))
year = str(datetime.date.strftime(yesterday, '%y%m%d'))
month = str(datetime.date.strftime(yesterday, '%m'))
day = str(datetime.date.strftime(yesterday, '%d'))
_user = "1599615269@qq.com"
_pwd = "tttqqzyzydqojjcc"
_to = "1084971261@qq.com,1599615269@qq.com,641999609@qq.com,312639695@qq.com,694949843@qq.com,lirenjie0519@qq.com"
# _to = "1599615269@qq.com"

#_to = "1223780226@qq.com"
_to = _to.split(',')

# 如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "%s_白班数据统计"%(yesterday)
msg["From"] = _user
msg["To"] = ",".join(_to)

# ---这是文字部分---
part = MIMEText("附件下载查看")
msg.attach(part)

# ---这是附件部分---
# xlsx类型附件
part = MIMEApplication(open("/opt/tools/create_log/%s/%s.xlsx"%(year,days), 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="%s.xlsx"%(days))
msg.attach(part)

s = smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=30,)  # 连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()