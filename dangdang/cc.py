# encoding='utf-8
# @Time: 2023-09-12
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
import execjs
import time


class dangdang():
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://login.dangdang.com',
            'Pragma': 'no-cache',
            'Referer': 'https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.12',
            'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.permanent_id = self.get_permanent_id()
        # print(self.permanent_id)
        self.time_stamp = self.get_time_stamp()
        self.requestId, self.rankey = self.get_randkey()
        # self.GetSlidingVerifyCode()
        self.sildeImg, self.bgImg, self.encryptKey, self.y = self.GetSlidingVerifyCode()
        print(self.sildeImg, self.bgImg, self.encryptKey, self.y)

    # 第一步获取__permanent_id

    def get_permanent_id(self):
        with open('./dangdang/__permanent_id.js', 'r', encoding='utf-8') as f:
            js = f.read()
        ctx = execjs.compile(js)
        __permanent_id = ctx.call('createPermanentID')
        return __permanent_id
    # 获取时间戳

    def get_time_stamp(self):
        return str(int(time.time()*1000))
    # 第二步 获取randkey, requestid, /getRankey

    def get_randkey(self):
        a = 'ct=pc&permanent_id={}&t={}'.format(
            self.permanent_id, self.time_stamp)
        with open('./dangdang/dd-AES.js', 'r', encoding='utf-8') as f:
            js = f.read()
        ctx = execjs.compile(js)
        sign = ctx.call('AesEncrypt', a, '')
        # print(sign)
        data = {
            't': self.time_stamp,
            'ct': 'pc',
            'permanent_id': self.permanent_id,
            'requestId': '',
            'sign': sign
        }

        response = self.session.post('https://login.dangdang.com/api/customer/loginapi/getRankey',
                                     data=data)
        return response.json()['requestId'], response.json()['rankey']
    # 第三步 获取图片验证码接口 /loginapi/getSlidingVerifyCode，图片验证码接口
    # 需要两张图片，一张是滑块，一张是背景，encryptKey，用于后面point_json AES加密的key, ‘y’用于后面point_json 需要被加密的参数

    def GetSlidingVerifyCode(self):
        timestamp = self.get_time_stamp()
        a = 'ct=pc&permanent_id={}&requestId={}&situation=login&t={}'.format(
            self.permanent_id, self.requestId, timestamp)
        # print(a)
        with open('./dangdang/dd-AES.js', 'r', encoding='utf-8') as f:
            js = f.read()
        ctx = execjs.compile(js)
        sign = ctx.call('AesEncrypt', a, self.rankey)
        # print(sign)
        data = {
            't': timestamp,
            'ct': 'pc',
            'permanent_id': self.permanent_id,
            'requestId': self.requestId,
            'situation': 'login',
            'sign': sign
        }
        response = self.session.post('https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode',
                        data=data)
        print(response.json())
        return response.json()['data']['slideImg'], response.json()['data']['bgImg'], response.json()['data']['encryptKey'], response.json()['data']['y']


if __name__ == "__main__":
    a = dangdang()
