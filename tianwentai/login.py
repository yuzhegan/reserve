# encoding='utf-8

# @Time: 2024-01-01
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import re

# gen code 

# gen wxuser
import requests

# print(len('041zmRkl25JJEc4rZqol2GIoI04zmRks'))
# exit()


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\""
}
url = "https://weather.121.com.cn/szqx/api/wx.do"
params = {
    "client": "sztw",
    "code": "091HM7000VcIkR1GYw000gEoRb1HM70u",
    "redirect_uri": "https://weather.121.com.cn/sztwt/#/gr"
}
response = requests.get(url, headers=headers, params=params)

# print(response.text)
# print(response)
# print 当前url
print("当前url",response.url)
