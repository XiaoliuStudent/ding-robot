#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 14:46
# @Author  : 刘航宇
# @File    : sendMessage.py
# @Description : 关于处理发送消息
from domain.dingdingToken import dingdingSession
from utils.getConfig import global_config


class PackText:
    def __init__(self):
        pass

    def packHelpDocs(self, message_text):
        """
        包装消息函数
        :param message_text: 需要包装的消息
        :return: 包装后的消息
        """
        message = message_text
        return message

    def packText(self):
        data = {
            "msgParam": '{"content": "你好"}',
            "msgKey": "sampleText",
            "openConversationId": "cidpVZDrUkklLmwfu4OeE7GEg==",
            "robotCode": "dingzhhaiuviurkjlqmx",
        }
        res = dingdingSession.session.post("https://api.dingtalk.com/v1.0/robot/groupMessages/send", json=data)
        print(res.json())
        pass


class PackMarkdown:
    def __init__(self):
        pass

    def packHelpDocs(self, message_text) -> str:
        md = """
# 查询的结果如下
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
 
引用
> A man who stands for nothing will fall for anything.
 
文字加粗、斜体
**bold**
*italic*
 
链接
[this is a link](https://www.dingtalk.com/)
 
图片
![](http://name.com/pic.jpg)
 
无序列表
- item1
- item2
 
有序列表
1. item1
2. item2
"""
        return md


class PackFile:

    def __init__(self):
        self.media_id1 = "@lArPDe7s_EkCjc_ODTYLTc5y6uD_"  # 测试docx文件
        self.media_id2 = "@lAnPDe7s_EkS6knOSiXGOs5460vC"  # 测试docx文件
        self.media_id3 = "@lAjPDf0i9t2tMyzOIk96Es5i2h_m"  # 松鼠ailogo
        pass

    def packDocFile(self, text, title, pic_url, message_url):
        data = {
            "msgParam": '"text": "消息内容测试","title": "sampleLink消息测试","picUrl": "@lAjPDf0i9t2tMyzOIk96Es5i2h_m","messageUrl": "http://dingtalk.com"}',
            "msgKey": "sampleLink",
            "openConversationId": "cidpVZDrUkklLmwfu4OeE7GEg==",
            "robotCode": "dingzhhaiuviurkjlqmx",
        }
        res = dingdingSession.session.post("https://api.dingtalk.com/v1.0/robot/groupMessages/send", json=data)
        print(res.json())
        pass


class PackUrl:
    def __init__(self):
        pass

    def packDocUrl(self, text, title, message_url, pic_url="@lAjPDf0i9t2tMyzOIk96Es5i2h_m"):
        data = {
            "msgParam": "{" + f'"text": "{text}","title": "{title}","picUrl": "{pic_url}","messageUrl": "{message_url}"' + "}",
            "msgKey": "sampleLink",
            "openConversationId": "cidpVZDrUkklLmwfu4OeE7GEg==",
            "robotCode": global_config['dingding']['client_id'],
        }
        res = dingdingSession.session.post("https://api.dingtalk.com/v1.0/robot/groupMessages/send", json=data)
        return res.json()


if __name__ == '__main__':
    # nihao = packFile()
    # nihao.packDocFile()
    packUrl = PackUrl().packDocUrl("win打印机使用说明", "win打印机使用说明",
                                   "https://docs.qq.com/doc/DYVVwSVFFeGh4UW5D")
    print(packUrl)
