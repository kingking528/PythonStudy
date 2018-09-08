#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
def is_valid_email(addr):
    re_mail = re.compile(r'^([0-9a-zA-Z][0-9a-zA-Z\_\.]{0,19})@([0-9a-zA-Z\]?).([0-9a-zA-Z])')
    return re_mail.match(addr)


addr = input('请输入测试E-mail地址：')
if is_valid_email(addr):
    print('OK')
else:
    print('Error')