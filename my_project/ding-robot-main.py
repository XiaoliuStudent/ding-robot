#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 11:09
# @Author  : 刘航宇
# @File    : ding-robot-main.py
# @Description :

def main():
    """
    authot: liuhangyu
    :return:
    """
    credential = dingtalk_stream.Credential('dingzhhaiuviurkjlqmx',
                                            'EGJ43Fidnln7paWAeHfPRUAnwQCaaW6VhLBy0GVIwIH7bpK851lLi2WWGOchrvpG')
    client = dingtalk_stream.DingTalkStreamClient(credential)
    client.register_all_event_handler(MyEventHandler())
    client.register_callback_handler(dingtalk_stream.chatbot.ChatbotMessage.TOPIC, CalcBotHandler())

    client.start_forever()


if __name__ == '__main__':

    main()
