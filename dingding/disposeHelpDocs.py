#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 14:46
# @Author  : 刘航宇
# @File    : disposeHelpDocs.py
# @Description : 关于处理消息帮助菜单

from domain.dingdingHelpDocs import DingDingHelpDocs
from utils.logUtil import logging


class DisposeHelpDocs:
    def __init__(self, message):
        self.message: str = message

    def getDocs(self) -> str:
        """
        获取帮助文档的内容
        :return:
        """
        tab_size = 0
        records = []
        # 如果为空则直接返回全部帮助文档
        if self.message == "" or self.message == "帮助文档":
            records = DingDingHelpDocs.select().where(DingDingHelpDocs.doc_type != 3,
                                                      DingDingHelpDocs.state == 1).order_by(
                DingDingHelpDocs.work_type)
            tab_size = 0
        # 返回具体命令的帮助文档
        else:
            # 判断输入的命令参数是否合法，如果不合法直接返回
            try:
                doc_name = self.message.split(" ")[1]
            except Exception as e:
                logging.warning(f"接收的命令或者参数不合法")
                return "命令或者参数不合符规范"

            # 判断输入的命令是否在数据库中存在
            try:
                record = DingDingHelpDocs.get(DingDingHelpDocs.doc_name == doc_name)
            except Exception as e:
                logging.warning(f"命令不存在")
                return "命令不存在"

            # 根据命令的类型返回消息
            if record.doc_type == "1":
                records = DingDingHelpDocs.select().where(
                    DingDingHelpDocs.work_type == record.work_type, DingDingHelpDocs.doc_type != 3,
                    DingDingHelpDocs.state == 1)
                tab_size = 1

            elif record.doc_type == "2":
                records = DingDingHelpDocs.select().where(DingDingHelpDocs.doc_name == doc_name + "详情",
                                                          DingDingHelpDocs.state == 1)
                tab_size = 3
        doc_text = ""
        for record in records:
            doc_text = doc_text + " " * (int(record.doc_type) - tab_size) + record.doc_comment + "\n"
        return doc_text


if __name__ == '__main__':
    print(DisposeHelpDocs("帮助文档").getDocs())
    print(DisposeHelpDocs("帮助 账户管理").getDocs())
    print(DisposeHelpDocs("帮助 创建账户").getDocs())
