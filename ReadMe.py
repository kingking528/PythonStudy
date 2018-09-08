#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# List  .append/.insert/.pop
names = ['Michael', 'Bob', 'Tracy']
L = ['Apple', 123, True]

#Dict  .get
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#tuple tuple的每个元素，指向永远不变
classmates = ('Michael', 'Bob', 'Tracy')
t = ('abc',)

#set  .add/.remove  没有value的dict
s = set([1, 2, 3])

#Function Parameters 必选参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f1(*args, **kw)

#Recursive Function
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
#fact(5)

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

# move(4, 'A', 'B', 'C')

#切片 Slice 替代Substring
L99 = list(range(100))
print(L99[:10]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L99[-10:])  #[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(L99[:10:2])  #[0, 2, 4, 6, 8]
print('ABCDEFG'[:3])  #'ABC'
print('ABCDEFG'[::2]) #'ACEG'

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    '''首先判断该字符串是否为空，如果为空，就返回该字符串，
    如果不为空的话，就判断字符串首尾字符是否为空，
    如果为空，就使用递归再次调用该函数trim(),否则就返回该函数'''
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return (trim(s[1:]))
    elif s[-1] == ' ':
        return (trim(s[:-1]))
    return s
#列表生成式
print(list(range(1, 11)))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x * x for x in range(1, 11) if x % 2 == 0])  #[4, 16, 36, 64, 100]
print([m + n for m in 'ABC' for n in 'XYZ']) #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])  #['hello', 'world', 'apple']

#生成器：generator
g = (x * x for x in range(10))
for n in g:
    print(n)

def triangles():
    N=[1]
    while True:
        yield N
        print(N)
        N.append(0)
        N=[N[i-1] + N[i] for i in range(len(N))]
n=0
for t in triangles():
    n=n+1
    if n == 10:
        break

#高阶函数   map()和reduce()函数
def normalize(x):  #变为首字母大写，其他小写的规范名字
    return x[:1].upper() + x[1:len(x)].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce #reduce 第一个参数为包含两个参数一个输出的函数，reduce依次调用
def AxB(a,b):
    return a * b
def prod(L):  #求积
    return reduce(AxB,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#filter 过滤：根据仅包含一个参数的“筛选”函数返回的bool值确定是否丢弃序列中的值
def is_palindrome(n): #验证回数
    return str(n)[:] == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

#排序 sorted
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

#匿名函数  lambda
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)
L_lambda = list(filter(lambda x:x%2==1, range(1, 20))) #与上一个写法等效，简洁
print(L)

#namedtuple 带名称的tuple子类
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
Circle = namedtuple('Circle', ['x', 'y', 'r'])
cir = Circle(2,2,5)

#deque 可以双向插入的list
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y') #['y', 'a', 'b', 'c', 'x']  .popleft()

# OrderedDict 排序的Dict 按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

#Counter 计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)  #Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})


from contextlib import contextmanager
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
#with语句首先执行yield之前的语句，因此打印出<h1>；
#yield调用会执行with语句内部的所有语句，因此打印出hello和world；
#最后执行yield之后的语句，打印出</h1>。
