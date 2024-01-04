#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-04 16:27
# @Author  : 刘航宇
# @File    : moduleBaseClass.py
# @Description :
class ModuleBaseClass:
    def __init__(self, command, params):
        self.command = command
        self.params = params
        self.params_dict = {}

        lines = params.split("\n")
        for i in lines:
            if i.strip():
                key, value = i.split(":", 1)
                self.params_dict[key] = value
