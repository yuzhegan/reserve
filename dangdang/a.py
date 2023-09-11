# encoding='utf-8
# @Time: 2023-09-11
# @File: %
#!/usr/bin/env
import execjs
import time
from icecream import ic
import os
import requests
def GenAesSign(randomkey, requestId):
    e = {
        # "t": 1694419158248,
        "ct": "pc",
        "permanent_id": "20230911142218827323294417821307852",
        "requestId": "2309111557244290NRtRvH_14ac"
    }
    t = int(time.time()*1000)
    if requestId:
        e["requestId"] = requestId
    e["t"] = t
    a = "ct=" + e["ct"] + "&" + "permanent_id=" + e["permanent_id"] + \
        "&" + "requestId=" + e["requestId"] + "&" + "t=" + str(e["t"])
    # config md5 function
    def md5(str):
        import hashlib
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        return m.hexdigest()
    a = md5(a)
    def GenSign(a):
        if randomkey:
            key = randomkey
        else:
            key = 'seqLuMppJOLCorlm'
        iv = '0102030405060708'
        with open("./dangdang/a.js", "r", encoding="utf-8") as f:
            js = f.read()
        ctx = execjs.compile(js)
        return ctx.call("GenAesString", a, key, iv)
    # print(GenSign(a))
    return GenSign(a)
    # sign = GenSign(a)
def GetRandomkey(sign):
    headers = {
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
    data = {
        # 't': '1694423072381',
        'ct': 'pc',
        'permanent_id': '20230911142218827323294417821307852',
        'requestId': '2309111557244290NRtRvH_14ac',
    }
    data['sign'] = sign
    t = int(time.time()*1000)
    data['t'] = t
    response = requests.post(
        'https://login.dangdang.com/api/customer/loginapi/getRankey', headers=headers,  data=data).json()
    print(response)
    return [response['rankey'], response['requestId']]




def Genpic(sign):
    headers = {
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
    data = {
      # 't': '1694418998549',
      'ct': 'pc',
      'permanent_id': '20230911142218827323294417821307852',
      'requestId': '2309111539495510SsxUxo_e985',
      'situation': 'login',
      # 'sign': 'U+2v2R2Ve0NIHgMz3XJ9jqfLHb/cWrpqIfxlRtoByhJC1JH+hWVSYnwVbsJ2vil2'
    }

    t = int(time.time()*1000)
    data['t'] = t
    data['sign'] = sign
    # data['requestId'] = requestId

    response = requests.post('https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode', headers=headers,  data=data).json()
    print(response)
if __name__ == "__main__":
    sign = GenAesSign('', '')
    randonkey, reqestid = GetRandomkey(sign)
    print(randonkey, reqestid)
    sign = GenAesSign(randonkey, reqestid)
    print(sign)
    Genpic(sign)
