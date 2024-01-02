#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 19:56
# @Author  : 刘航宇
# @File    : logUtil.py
# @Description : 日志工具
import logging

# 配置日志
logging.basicConfig(level=logging.INFO,  # 设置日志级别为 DEBUG，可以根据需要调整
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    logging.info("nihao")
