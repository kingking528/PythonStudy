#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
from analyzeMail import print_info

# 输入邮件地址, 口令和POP3服务器地址:
email = '7258136@qq.com'
password = 'anaiyaanbtexcbdb'
pop3_server = 'pop.qq.com'  #995 ssl

# 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server,'995')
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]

# 获取最新一封邮件, 注意索引号从1开始:
for index in range(len(mails)):
    resp, lines, octets = server.retr(index+1)
    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    print_info(msg)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()




