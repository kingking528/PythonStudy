#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Created Date: 2018-09-08,Saturday 01:01:56
# Author: YangXu
# Last Modified: 2018-09-17,Monday 10:16:18
# Modified By: YangXu
###

while True:
    salary = input("Salary:")
    try:
        salary = float(salary)
        print("Salary : %f" % salary)
        break
    except ValueError:
        print("Wrong input,please input a number!")
        continue