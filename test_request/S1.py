#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 19:36
# @Author : 不爱码代码的码农
# @Site : 
# @File : S1.py
# @Software: PyCharm
import json

import requests



def get_response_strem(url):

    """
    将文本流保存到文件
    :param url:
    """
    r = requests.get(url)
    with open("data", "wb") as fw:
        for chunk in r.iter_content(chunk_size=10000):
            fw.write(chunk)

def get_response(url):
    """
    response 以json形式写入文件
    :param url:
    """
    r = requests.get(url=url)
    content_json = r.json()
    print(type(content_json))
    with open("github.json", 'w') as fw:
        json.dump(content_json, fw)


if __name__ == '__main__':
    url = 'https://api.github.com/events'
    # get_response(url)
    r = requests.get(url=url)
    r.encoding = "GBK" # 改变文件编码
    # 字节形式返回response
    # print(r.content)
    print(r.cookies)

