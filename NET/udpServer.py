#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 9999
# 绑定端口:
s.bind(('127.0.0.1', port))

print('Bind UDP on ' , str(port) , '...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    print('Received Data :', data.decode('utf-8'))
    s.sendto(b'Hello, %s!' % data, addr)