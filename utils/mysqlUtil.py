#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 10:50
# @Author  : 刘航宇
# @File    : mysqlUtil.py
# @Description : this is mysql util
# 用于mysql数据库的链接，并创建连接池和实例

from playhouse.pool import PooledMySQLDatabase
from utils.getConfig import global_config

db = PooledMySQLDatabase(database=global_config['mysql']['database'],
                         user=global_config['mysql']['username'],
                         password=global_config['mysql']['password'],
                         host=global_config['mysql']['host'],
                         port=int(global_config['mysql']['port']),
                         stale_timeout=10,
                         max_connections=1)
