from domain.dingdingToken import access_token
import requests

import tkinter as tk
from tkinter import filedialog


def getFilePath():
    """
    获取上传文件的路径
    :return:
    """
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    file_path = filedialog.askopenfilename()

    if file_path:
        return file_path
    else:
        exit(1)


# 获取文件位置
filePath = getFilePath()
# 配置文件上传的参数
files = {
    'media': (filePath.split("/")[0], open(filePath, 'rb')),  # （文件名，文件二进制流）
    'type': (None, 'file'),  # 固定格式，不需要改
}
# 上传文件
response = requests.post("https://oapi.dingtalk.com/media/upload", params={'access_token': access_token}, files=files)

print(response.json())
