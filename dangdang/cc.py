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
        self.data = {
            # 't': '1694423072381',
            'ct': 'pc',
            'permanent_id': "20230911142218827323294417821307852",
            'requestId': "2309121434209380Iu3zZD_50e1",
        }
        # self.GenerateSign(ifbg=False)
        self.IsSlide()
        # self.GenerateSign(t = '1694500674507',ifbg=True)
        requesid, randkey = self.GetRandomKey()
        self.GetSildVerifyCode(requesid,randkey)
        

    # md5加密

    def encryptMd5(self, str):
        import hashlib
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        return m.hexdigest()
    # AES加密

    def encryptAES(self, string, randomkey, iv):
        with open("./dangdang/a.js", 'r', encoding='utf-8') as f:
            js = f.read()
        jscode = execjs.compile(js)
        sign = jscode.call('GenAesString', string, randomkey, iv)
        return sign

    def GenerateSign(self, t, randkey, ifbg=False):
        if t:
            t = t
        else:
            t = str(int(time.time()*1000))
        self.data['t'] = t
        if ifbg:
            a = "ct=" + self.data["ct"] + "&" + "permanent_id=" + self.data["permanent_id"] + \
                "&" + "requestId=" + self.data["requestId"] + \
                "&situation=login&" + "t=" + str(self.data["t"])
        else:
            a = "ct=" + self.data["ct"] + "&" + "permanent_id=" + self.data["permanent_id"] + \
                "&" + "requestId=" + \
                self.data["requestId"] + "&" + "t=" + str(self.data["t"])
        print(a)
        md5a = self.encryptMd5(a)
        print(md5a)
        if randkey:
            randkey = randkey
        else:
            randkey = "Lyi8ARQhISYjbnl0"
        iv = '0102030405060708'
        sign = self.encryptAES(md5a, randkey, iv)
        print(sign)
        return sign

    def IsSlide(self):
        data = {
            # 't': '1694495768902',
            'ct': 'pc',
            'permanent_id': '20230911142218827323294417821307852',
            'requestId': '2309121304209620jk9OfC_676c',
            'sign': 'eo0fr5Fx098/yS7ogjhlKuN0RPmHlcEScKrIhRIJFnxKv3rr7IDRW0HJwFYviUO4'
        }
        t = str(int(time.time()*1000))
        data['t'] = t
        sign = self.GenerateSign('','', ifbg=False)
        print(sign)
        response = self.session.post(
            'https://login.dangdang.com/api/customer/loginapi/isShowSlide', data=data).json()
        print(response)

    def GetSildVerifyCode(self, requestId, randkey):
        data = {
            # 't': '1694495769595',
            'ct': 'pc',
            'permanent_id': '20230911142218827323294417821307852',
            'requestId': '2309121304209620jk9OfC_676c',
            'situation': 'login',
            # 'sign': 'YLuqsWIJYrxrArHylpkWH5mkQ7kE1NDHOmcGTuPTsEQ0MWwT+aN9CaQQHl6mKfNP'
        }
        if requestId:
            data['requestId'] = requestId


        t = str(int(time.time()*1000))
        data['t'] = t
        sign = self.GenerateSign('',randkey, ifbg=True)
        print(sign)
        data['sign'] = sign
        response = self.session.post(
            'https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode', data=data).json()
        print(response)

    def GetRandomKey(self):
        data = {
            # 't': '1694496861834',
            'ct': 'pc',
            'permanent_id': '20230911142218827323294417821307852',
            'requestId': '2309121304209620jk9OfC_676c',
            # 'sign': 'bCSUTL+s9SVO21wlzWSjG8gc8CU5cefT0QPnDipbBwUdIsdt6ON8MuJaTyn3u84f'
        }
        t = str(int(time.time()*1000))
        data['t'] = t
        response = requests.post(
            'https://login.dangdang.com/api/customer/loginapi/getRankey',data=data).json()
        requestid = response['requestId']
        rankey = response['rankey']
        return requestid, rankey
        # print(response)

if __name__ == "__main__":
    a = dangdang()
