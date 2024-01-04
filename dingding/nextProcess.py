#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-04 14:53
# @Author  : 刘航宇
# @File    : nextSetp.py
# @Description :

from domain.docCommand import DocCommands
from dingding.importModules import *

from modules.document.document import Document

class NextProcess:
    def __init__(self):
        self.command = ""
        self.params = ""

    def nextDocumentProcess(self, doc_command):
        """
        处理文档命令
        :param doc_command:
        :param message:
        :return:
        """
        # 查询命令和参数
        abs_command = DocCommands.select().where(DocCommands.doc_name == doc_command)
        # 错误处理，如果查不到我唯一命令返回错误
        if len(abs_command) != 1: return "命令错误，该命令不是唯一命令，请检查数据库和输入的字段"

        # 获取命令和参数
        self.command = abs_command[0].command
        self.params = abs_command[0].params

        # 调用逻辑实例
        object_body, object_func = command_dict[abs_command[0].command]  # 根据命令拿到类和方法
        object_body = object_body(self.command, self.params)

        # 调用逻辑方法
        cmd_result = object_func(object_body)

        return cmd_result

    def nextTransProcess(self):
        """
        处理事务命令
        :return:
        """
        pass


if __name__ == '__main__':
    document = NextProcess().nextDocumentProcess("连接打印机")
