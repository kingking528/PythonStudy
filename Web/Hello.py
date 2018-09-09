
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    with open('test.html', 'r', encoding='utf-8', errors='ignore') as f:  # r:读取成str  rb:读取二进制(不能编码) 
        b = bytes(f.read(), encoding = "utf8")
        ret = []
        ret.append(b)
        #ret = [b'<h1>Hello, web!</h1>']
        return ret