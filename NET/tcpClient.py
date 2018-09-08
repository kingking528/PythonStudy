#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IPv4,AF_INET6 - IPv6, SOCK_STREAM-TCP, SOCK_DGRAM-UDP
# 建立连接:
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    #处理数据
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

"""
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)


# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('test.html', 'wb') as f:
    f.write(html)

"""