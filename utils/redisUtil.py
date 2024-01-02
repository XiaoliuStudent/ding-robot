#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 11:02
# @Author  : 刘航宇
# @File    : redisUtils.py
# @Description : this is redis connect util
# 用于连接redis连接池
import redis
from getConfig import global_config

pool = redis.ConnectionPool(host=global_config['redis']['host'], port=global_config['redis']['port'], db=0,
                            decode_responses=True, max_connections=10)
redis = redis.Redis(connection_pool=pool)
