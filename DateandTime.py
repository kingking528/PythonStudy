#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime,timedelta

nowDate = datetime.now()
userDate = datetime(2018,9,30)
strDate = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
strDate = strDate.strptime('2018-10-1', '%Y-%m-%d') 
print(strDate)
print(nowDate.timestamp())
print(str(nowDate))
print(nowDate.strftime('%Y-%m-%d, %A, %B, %j')) #j-Day of the year as a zero-padded decimal number
userDate = nowDate + timedelta(weeks=2,days=2, hours=12)
print(userDate.strftime('%Y-%m-%d, %A, %B, %j')) #j-Day of the year as a zero-padded decimal number
print(timedelta(days=1,hours=2,seconds=3).total_seconds())