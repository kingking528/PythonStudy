#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Created Date: 2018-09-17,Monday 10:01:24
# Author: YangXu
# Last Modified: 2018-09-17,Monday 10:11:34
# Modified By: YangXu
###

def login(uName,pWord):
    return uName == "King" and pWord == "123456" 

n = 0
while True:
    n += 1
    uName = input("Please input user name:")
    pWord = input("Please input password:")
    if login(uName,pWord):
        print("Welcome! %s" % uName)
        break
    else:
        print("Invalid username or password !")
    if n >= 5:
        print("Try too many times! Get out !")
        break