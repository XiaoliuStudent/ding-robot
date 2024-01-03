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


# 装饰器函数
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} completed with result: {result}")
        return result

    return wrapper


if __name__ == "__main__":
    logging.info("nihao")
