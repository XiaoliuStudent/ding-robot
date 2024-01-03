#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-02 14:46
# @Author  : 刘航宇
# @File    : sendMessage.py
# @Description : 关于处理发送消息

class packText:
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


class packMarkdown:
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


class packFile:
    def __init__(self):
        pass

    def packDocFile(self):
        pass


if __name__ == '__main__':
    print(packMarkdown().packHelpDocs("nihao"))
