#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-03 17:44
# @Author  : 刘航宇
# @File    : transcation.py
# @Description : 处理事务逻辑
import datetime

from peewee import *

from utils.mysqlUtil import db


class Transaction(Model):
    """
    事务的实体
    下述的实体与数据库字段完全一致
    """
    transaction_id = CharField(primary_key=True)

    class Meta:
        database = db
        table_name = 'transactions'

    def makeId(self):
        self.transaction_id = str(datetime.datetime.now()).replace("-", "").replace(" ", "").replace(":", "")[6:12]
        return self.transaction_id
