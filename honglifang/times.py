# encoding='utf-8
# @Time: 2023-10-28
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import time
import argparse
import ast
# 创建参数解析器
import ast
def convert_to_dict(string):
    try:
        dictionary = ast.literal_eval(string)
        if isinstance(dictionary, dict):
            return dictionary
        else:
            raise ValueError('提供的字符串不是一个有效的字典格式。')
    except SyntaxError:
        raise ValueError('提供的字符串不是一个有效的字典格式。')
string = "{'http': 'http://221.229.53.141:6727', 'https': 'https://221.229.53.141:6727'}"
proxies = convert_to_dict(string)
print(proxies)
