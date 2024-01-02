#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 14:46
# @Author  : 刘航宇
# @File    : disposeHelpDocs.py
# @Description : 关于处理消息帮助菜单

from domain.dingdingHelpDocs import DingDingHelpDocs


class DisposeHelpDocs:
    def __init__(self, message):
        self.message: str = message
        self.text: str = ""
        self.doc_type: 0
        self.error = 0
        self.result = "aadda"

        # 查询全部记录
        if self.message == "" or "帮助文档" in self.message:
            records = DingDingHelpDocs.select().where(DingDingHelpDocs.doc_type != 3).order_by(
                DingDingHelpDocs.work_type)
            self.disposeDocs(records, 0)
        # 根据命令名字匹配记录
        else:
            # 首先判断命令是否存在于数据库中
            try:
                record = DingDingHelpDocs.get(DingDingHelpDocs.doc_name == self.getDocName())
            except Exception as e:
                self.error = 1
                self.result = "命令错误"
                return
            # 判断命令是一级命令或者二级命令
            if record.doc_type == "1":
                records = DingDingHelpDocs.select().where(
                    DingDingHelpDocs.work_type == record.work_type, DingDingHelpDocs.doc_type != 3)
                self.disposeDocs(records, 1)

            elif record.doc_type == "2":
                records = DingDingHelpDocs.select().where(DingDingHelpDocs.doc_name == self.getDocName() + "详情")
                text = ""
                for record in records:
                    text = text + record.doc_comment + "\n"
                self.text = text

        # 根据记录名字查询
        # print(record.doc_id)

    def getDocName(self):
        """
        获取名字l文档名字
        :return: 命令名字
        """
        doc_name = self.message.split(" ")[1]
        return doc_name

    def getDocs(self):
        return self.text

    def disposeDocs(self, records, tab):
        text = ""
        for record in records:
            text = text + " " * (int(record.doc_type) - tab) + record.doc_comment + "\n"
        self.text = text


if __name__ == '__main__':
    print(DisposeHelpDocs("").getDocs())
    print(DisposeHelpDocs("帮助 账户管理").getDocs())
    print(DisposeHelpDocs("帮助 创建账户").getDocs())
