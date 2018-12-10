#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from datetime import datetime,timedelta

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'kingking528@126.com'
password = 'yx840528'
to_addr = '7258136@qq.com'
smtp_server = 'smtp.126.com'

msg = MIMEText('Pyrhon测试邮件20180909 \r\n发送时间：%s' % datetime.now().strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'), 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('Pyrhon测试邮件', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()