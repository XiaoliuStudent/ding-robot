#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-04 15:32
# @Author  : 刘航宇
# @File    : nihao.py
# @Description :

# 导入模块
from modules.document.document import Document  # 导入打印机模块

# 管理命令与实例和方法
command_dict = {
    "send_file": (Document, Document.sendDocument)
}
