#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-03 17:34
# @Author  : 刘航宇
# @File    : getDate.py
# @Description :
import datetime

print(str(datetime.datetime.now()).replace("-", "").replace(" ", "").replace(":", ""))
print(str(datetime.datetime.now()).replace("-", "").replace(" ", "").replace(":", "")[6:12])
