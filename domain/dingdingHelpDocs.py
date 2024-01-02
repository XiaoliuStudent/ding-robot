#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 13:56
# @Author  : 刘航宇
# @File    : dingdingHelpDocs.py
# @Description : 关于钉钉机器人帮助文档实体
from datetime import datetime

from peewee import *
from utils.mysqlUtil import db


class DingDingHelpDocs(Model):
    """
    下述的实体与数据库字段完全一致
    """
    doc_id = CharField(primary_key=True)
    doc_name = CharField(null=False)
    doc_type = CharField(null=False)
    work_type = CharField(null=False)
    father_doc_id = CharField(null=False)
    doc_comment = CharField(null=False)
    state = CharField(null=False)
    create_time = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'help_docs'


if __name__ == '__main__':
    for i in DingDingHelpDocs.select():
        print(i, i.doc_name)
