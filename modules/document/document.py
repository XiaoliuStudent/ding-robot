#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-04 15:03
# @Author  : 刘航宇
# @File    : printerImpl.py
# @Description :
from dingding.packMessage import PackUrl
from modules.moduleBaseClass import ModuleBaseClass


class Document(ModuleBaseClass):
    def sendDocument(self):
        packUrl = PackUrl()
        packUrl.packDocUrl(self.params_dict['text'], self.params_dict['title'], self.params_dict['url'])
        return "执行成功"

    def __init__(self, command, params):
        super().__init__(command, params)


if __name__ == '__main__':
    # nihao = PrinterImpl("comm","com_params")
    # nihao.sendDocument()

    nihao = Document("comm", "com_parms")
    aaa = Document.sendDocument(nihao)
    print(aaa)
