#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 11:13
# @Author  : 刘航宇
# @File    : ding-robot-main.py
# @Description :
import dingtalk_stream
from dingtalk_stream import AckMessage
from utils.getConfig import global_config


class AllEventHandler(dingtalk_stream.EventHandler):
    """
        所有事件监听器
    """

    async def process(self, event: dingtalk_stream.EventMessage):
        """
        事件处理
        :param event:
        :return:
        """
        print(event.headers.event_type)
        print(event.headers.event_id)
        print(event.headers.event_born_time)
        print(event.data)
        print(event)
        return AckMessage.STATUS_OK, 'OK'


class CallBackHandler(dingtalk_stream.ChatbotHandler):
    """
    所有消息监听器
    """

    async def process(self, callback: dingtalk_stream.CallbackMessage):
        """
        消息处理
        :param callback:
        :return:
        """
        incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
        # 拿到消息正文
        message = incoming_message.text.content.strip()
        # 回复消息
        self.reply_text("this is test ok", incoming_message)
        return AckMessage.STATUS_OK, 'OK'


if __name__ == '__main__':
    """
        项目启动入口，创建钉钉监听实例
    """
    credential = dingtalk_stream.Credential(global_config['dingding']['client_id'],
                                            global_config['dingding']['client_secret'])
    client = dingtalk_stream.DingTalkStreamClient(credential)
    # 监听所有事件
    client.register_all_event_handler(AllEventHandler())
    # 监听消息事件
    client.register_callback_handler(dingtalk_stream.chatbot.ChatbotMessage.TOPIC, CallBackHandler())
    # 启动监听
    print("启动监听")
    client.start_forever()
