#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import itertools,time
def pi(N):
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= N, natuals)
    l = list(ns)
    for i in range(len(l)):
        if l[i] % 2 == 1:
            l[i] = 4 / (l[i] * 2 - 1)
        else:
            l[i] = - 4 / (l[i] * 2 - 1)
    return sum(l)

# 测试:
start = time.time()
print(pi(999999))
end = time.time()
print('使用时间：',end-start)