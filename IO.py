#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 'ABC'
b = bytes(x,encoding='utf-8')  #字符串变bytes

with open('README.md', 'r', encoding='utf-8', errors='ignore') as f:  # r:读取成str  rb:读取二进制(不能编码) 
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

with open('README.md', 'a', encoding='utf-8') as f:   # a:append w:overwrite  wb:写入二进制
    f.write('\nHello, world!')


fpath = r'C:\Windows\system.ini'   #将本地一个文本文件读为一个str并打印出来
with open(fpath, 'r') as f:
    s = f.read()
    print(s)



from io import StringIO #StringIO
f = StringIO()
f.write('ABCD')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
     s = f.readline()
     if s == '':
         break
     print(s.strip())

from io import BytesIO  #BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())



import os
#print(os.name)
#print(os.environ)
#print(os.path.abspath('.'))  #G:\Codes\PythonStudy
print(os.path.join(r'G:\Codes\PythonStudy', 'testdir'))  # G:\Codes\PythonStudy\testdir
print(os.path.join(r'G:\Codes\PythonStudy', 'a.txt'))  # G:\Codes\PythonStudy\a.txt
print(os.path.split(r'G:\Codes\PythonStudy\a.txt'))  #('G:\\Codes\\PythonStudy', 'a.txt')
print(os.path.splitext(r'G:\Codes\PythonStudy\a.txt'))  #('G:\\Codes\\PythonStudy\\a', '.txt')
print([x for x in os.listdir('.') if os.path.isdir(x)])   #列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])  #列出所有的.py文件


import pickle #Python专用的序列化
d = dict(name='Bob', age=20, score=88)
b = pickle.dumps(d) #pickle.dumps() 序列化成一个bytes pickle.dump(d,f) 序列化d写入f
print(b)  
dx = pickle.loads(b) #pickle.loads() bytes反序列化为对象，pickle.load()对应可读的file-like Object，比如文件流或者内存流
print(dx)

import json #Json序列化
d = dict(name='Bob', age=20, score=88)
json_s = json.dumps(d)  #dumps()方法返回一个str，内容就是标准的JSON  dump()方法可以直接把JSON写入一个file-like Object
print(json_s)
dx = json.loads(json_s) #loads()把JSON的字符串反序列化，load()从file-like Object中读取字符串并反序列化
print(dx)

#类的对象的序列化相对麻烦一些：
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Anne', 22, 98)
j_s = json.dumps(s, default=lambda x: x.__dict__)  # default=lambda x: x.__dict__ 将类变成dict
print(j_s)

#ensure_ascii=True
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)  #{"name": "\u5c0f\u660e", "age": 20}
s = json.dumps(obj, ensure_ascii=False)  #{"name": "小明", "age": 20}
print(s)
