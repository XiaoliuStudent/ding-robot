#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 13:56
# @Author  : 刘航宇
# @File    : docCommand.py
# @Description : 关于钉钉机器人帮助文档实体
from datetime import datetime

from peewee import *
from utils.mysqlUtil import db


class DocCommands(Model):
    """
    命令和文档实体
    下述的实体与数据库字段完全一致
    """
    doc_id = CharField(primary_key=True)
    doc_name = CharField(null=False)
    doc_type = CharField(null=False)
    work_type = CharField(null=False)
    role = CharField(null=False)
    params = CharField(null=False)
    state = CharField(null=False)
    create_time = DateTimeField(default=datetime.now)
    command = CharField(null=False)

    class Meta:
        database = db
        table_name = 'doc_commands'


if __name__ == '__main__':
    for i in DocCommands.select():
        print(i, i.doc_name)
