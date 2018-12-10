#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s1 = input('身高（m）：')
s2 = input('体重（kg）：')
bmi = float(s2)/(float(s1)**2)
print('你的BMI指数为：{}'.format(bmi))
if bmi<18.5:
    ss = '过轻'
elif bmi<=25:
    ss = '正常'
elif bmi<=28:
    ss = '过重'
elif bmi<=32:
    ss = '肥胖'
else:
    ss = '严重肥胖'
print(ss)

for i in range(10):
    if i == 5:
        print('found it! i = %s' % i)
        break
else:
    print('not found it ...')