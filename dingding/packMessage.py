#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 14:46
# @Author  : 刘航宇
# @File    : sendMessage.py
# @Description : 关于处理发送消息
class PackMessage:
    def __init__(self):
        pass

    def packText(self, message_text) -> str:
        """
        包装消息函数
        :param message_text: 需要包装的消息
        :return: 包装后的消息
        """
        message = message_text
        return message

    def packMarkdown(self, message_text) -> str:
        return ""


if __name__ == '__main__':
    print(PackMessage().packText("this is test message"))
