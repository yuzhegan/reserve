# encoding='utf-8
# @Time: 2023-10-21
# @File: %
#!/usr/bin/env
from icecream import ic
import os
# get sild and bg img
import requests
headers = {
    'authority': 'iv.jd.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://passport.jd.com/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
params = (
    ('appId', '1604ebb2287'),
    ('scene', 'login'),
    ('product', 'click-bind-suspend'),
    ('e', '2PYVLZL3WDVBPL4LTF566N6PRFNAYO447LKWBQZATTYTUT5D6LCLYAD3O4S5PBY5ILNDQOU6SYXWTO3ZMQBVVXYL5I'),
    ('j', ''),
    ('lang', 'zh_CN'),
    ('callback', 'jsonp_06534497191746693'),
)
response = requests.get('https://iv.jd.com/slide/g.html', headers=headers, params=params).text

# str to json
import json
response = response.replace('jsonp_06534497191746693(', '')
response = response.replace(')', '')
response = json.loads(response)
ic(response)
bg = response['bg']
patch = response['patch']
# base64 to img
import base64
bg = base64.b64decode(bg)
with open('./jdlogin/img/bg.png', 'wb') as f:
    f.write(bg)
patch = base64.b64decode(patch)
with open('./jdlogin/img/patch.png', 'wb') as f:
    f.write(patch)

# get the instance of sild in bg img
import ddddocr
det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
bg = open('./jdlogin/img/bg.png', 'rb').read()
patch = open('./jdlogin/img/patch.png', 'rb').read()
instance = det.slide_match(patch, bg, simple_target=True)['target'][0]
ic(instance)


challenge = response['challenge']
y = response['y']




