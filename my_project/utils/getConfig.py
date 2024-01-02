#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 10:35
# @Author  : 刘航宇
# @File    : getConfig.py
# @Description : this is get config utils
import os
import yaml

# 定义全局配置变量和读取参数配置文件
global_config = {}
with open('../configs/globalConfig.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

# 判断当前环境，如果是开发则读取开发，否则读取生产环境配置文件
if os.getenv('ding-robot-env') == "dev":
    global_config = config_data['dev']
else:
    global_config = config_data['production']

# 测试实例
if __name__ == '__main__':
    print(global_config)
