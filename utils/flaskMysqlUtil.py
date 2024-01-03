#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-03 11:11
# @Author  : 刘航宇
# @File    : flaskMysqlUtil.py
# @Description :
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:nihaonihao000...@doisnot.com:3306/ding-robot?charset=utf8"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_BINDS '] = {"mysql": "mysql://root:"}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_BINDS'] = {'bind1': 'sqlite:///:memory:'}

# 创建组件对象
db = SQLAlchemy(app)


# 构建模型类  商品表
class Goods(db.Model):
    __tablename__ = 'help_docs'  # 设置表名
    doc_id = db.Column(db.String(100), primary_key=True)  # 设置主键
    doc_name = db.Column(db.String(1000))  # 商品名称


goods = Goods.query()
for i in goods:
    print(i)
