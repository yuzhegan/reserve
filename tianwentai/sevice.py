# encoding='utf-8
# @Time: 2024-01-02
# @File: %
#!/usr/bin/env
from icecream import ic
import os
from flask import Flask, request
app = Flask(__name__)


@app.route('/api/msg', methods=['POST'])
def receive_message():
    data = request.get_json()# 获取POST请求的JSON数据
    event = data.get('event')# 获取event字段的值
    if event == 10009:
        msg = data['data']['data']['msg']# 提取data.data.msg字段的值
        print(msg)# 打印消息内容
        start_index = msg.find('<shareUrlOpen>') + len('<shareUrlOpen>')
        end_index = msg.find('</shareUrlOpen>')
        content = msg[start_index:end_index]
        if len(content) > 0:
            print(content)
        else:
            print("content is empty")
    return 'Message received'# 返回响应


if __name__ == '__main__':
    app.run(port=12589)
