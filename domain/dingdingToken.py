#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-03 19:10
# @Author  : 刘航宇
# @File    : dingdingToken.py
# @Description : 管理钉钉API token
import datetime
import logging
import time

import requests
from utils.getConfig import global_config
from peewee import *

from utils.mysqlUtil import db


class DingDingSession(Model):
    app_key = CharField(primary_key=True, default=global_config['dingding']['client_id'])
    app_secret = CharField(null=False, default=global_config['dingding']['client_secret'])
    app_token = CharField(null=False)
    expire_time = DateTimeField(null=False)

    class Meta:
        database = db
        table_name = 'access_tokens'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.token_json = {
            "appkey": self.app_key,
            "appKey": self.app_key,
            "appsecret": self.app_secret,
            "appSecret": self.app_secret,

        }

    def getToken(self):
        """
        实现获取api 老版本和新版本的实现 并存放在数据库中
        :return:
        """
        # 老API接口
        res = self.session.get("https://oapi.dingtalk.com/gettoken", params=self.token_json)
        self.app_token = res.json()['access_token']
        self.session.headers['access_token'] = self.app_token

        # 新API接口
        res = self.session.post("https://api.dingtalk.com/v1.0/oauth2/accessToken", json=self.token_json)
        self.app_token = res.json()['accessToken']
        self.session.headers['x-acs-dingtalk-access-token'] = self.app_token

        logging.info("dingding token 获取成功")

    def setToken(self):
        """
        用于将获取的token保存在数据库中
        :return:
        """
        # 获取token
        self.getToken()

        #  首先判断数据库是否有该密钥的记录
        records = DingDingSession.select().where(DingDingSession.app_key == self.app_key)
        if len(records) == 0:
            # 不存在，进行增加
            DingDingSession.create(app_key=self.app_key, app_secret=self.app_secret)

        # 存在则进行更新操作
        nihao = DingDingSession.update(app_token=self.app_token,
                                       expire_time=datetime.datetime.now() + datetime.timedelta(hours=2)).where(
            DingDingSession.app_key == self.app_key).execute()

        # 结果判断
        if nihao != 1:
            logging.info("dingding token 更新到数据库成功")
        else:
            logging.info("dingding token 更新到数据库失败")


# 创建全局唯一实例
dingdingSession = DingDingSession()
# 紧接更新token
dingdingSession.setToken()
access_token_json = {'access_token': dingdingSession.app_token}
access_token = dingdingSession.app_token

if __name__ == '__main__':
    v1 = DingDingSession()
    v1.setToken()
    print(v1.app_token)

    # v1.setToken()
    # for i in v1.select():
    #     print(i.app_key)
