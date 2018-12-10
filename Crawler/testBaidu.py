#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# Created Date: 2018-12-09,Sunday 12:32:49
# Author: YangXu
# Last Modified: 2018-12-10,Monday 11:40:04
# Modified By: YangXu
###
import urllib2

url = 'http://www.google.com'
req = urllib2.Request(url)
# //req.add_header("apikey","33481140591d83456d6486e55fb00686")
resp = urllib2.urlopen(req)
content = resp.read()
if content:
    print(content)