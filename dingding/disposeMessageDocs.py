#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 14:46
# @Author  : 刘航宇
# @File    : disposeHelpDocs.py
# @Description : 关于处理消息帮助菜单

from domain.docCommand import DocCommands


class DisposeMessageDocs:
    """
    用于处理消息，判断消息命令是绝对命令或者模糊查询
    """

    def __init__(self):
        self.message_type = ""


    def getDocs(self, receive_message) -> str:
        """
        实例消息实现
        :param receive_message: 获取的消息
        :return: 命令查询数据库的结果
        """
        # 输入去污
        receive_message = receive_message.replace("：", ":").lower()
        command_message = "查询的结果如下：\n"
        # 首先判断命令中是否含有参数，判断依据 “  : ”
        if ":" in receive_message:
            self.message_type = "携带参数的绝对事务命令"
            return "已经拿到了参数和命令，即将进行下一步"

        # 再次判断该发送的消息是否是绝对命令
        abs_command = DocCommands.select().where(DocCommands.doc_name == receive_message)
        if len(abs_command) != 0:
            if abs_command[0].role == "0":
                self.message_type = "绝对文档类命令"
                command_message = "绝对文档类命令，即将进行下一步"
            else:
                self.message_type = "绝对事务命令"
                command_message = "该命令的模板如下：\n\n" + abs_command[0].params_dict + "\n\n请复制该模板到输入框中，填写参数，并提交"
            return command_message

        # 模糊命令
        commands = DocCommands.select().where(
            DocCommands.doc_name.contains(receive_message) | DocCommands.work_type.contains(
                receive_message) | DocCommands.params.contains(receive_message),
            DocCommands.doc_type == "3")

        # 查询不到匹配的命令
        if len(commands) == 0:
            self.message_type = "查询不到匹配命令"
            command_message = command_message + "输入的关键词在数据库中查询不到类似的命令！"

        # 返回匹配到的命令
        for i in commands:
            self.message_type = "模糊命令"
            command_message = command_message + "- " + i.doc_name + "\n"

        return command_message


if __name__ == '__main__':
    # print(DisposeHelpDocs("帮助文档").getDocs())
    # print(DisposeHelpDocs("帮助 账户管理").getDocs())
    # print(DisposeHelpDocs("帮助 创建账户").getDocs())

    print(DisposeMessageDocs().getDocs("申请："))
