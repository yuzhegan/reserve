# encoding='utf-8
# @Time: 2023-10-21
# @File: %
#!/usr/bin/env
from gentrace import get_trace
import ddddocr
import base64
import re
import json
from icecream import ic
import time
import os
# get sild and bg img
import requests
headers = {
    'authority': 'iv.jd.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://passport.jd.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
# params = {
#     'ReturnUrl': 'https://www.jd.com/',
# }
# response = requests.get('https://passport.jd.com/new/login.aspx', params=params, headers=headers)
# # get the cookies in response
# cookies = response.cookies
# ic(cookies)


params = {
    'appId': '1604ebb2287',
    'scene': 'login',
    'product': 'click-bind-suspend',
    'e': 'FHWFGUXTWJQDJ7VQMTQK243QCO43XEC5CRGLGTKMVTAV7GWKCPSTIEGSFTX2WRFTUSGB4DUXDFINJJWXQW7IYCPHMU',
    'j': '',
    'lang': 'zh_CN',
    'callback': 'jsonp_047453865740509427',
}
response = requests.get('https://iv.jd.com/slide/g.html',
                        params=params,  headers=headers).text
# str to json
# response = response.replace('jsonp_07097674328611292(', '')
# response = response.replace(')', '')
# 原始字符串
# 使用正则表达式匹配 JSON 数据
pattern = r'\((.*?)\)'  # 匹配括号内的内容
match = re.search(pattern, response)
if match:
    response = match.group(1)
else:
    print("No JSON data found.")
response = json.loads(response)
# ic(response)
bg = response['bg']
patch = response['patch']
# base64 to img
bg = base64.b64decode(bg)
with open('./jdlogin/img/bg.png', 'wb') as f:
    f.write(bg)
patch = base64.b64decode(patch)
with open('./jdlogin/img/patch.png', 'wb') as f:
    f.write(patch)
# get the instance of sild in bg img
det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
bg = open('./jdlogin/img/bg.png', 'rb').read()
patch = open('./jdlogin/img/patch.png', 'rb').read()
instance = det.slide_match(patch, bg, simple_target=True)['target'][0]
instance = round(instance*242/360+23)
ic(instance)
challenge = response['challenge']
# y = response['y']
trace = get_trace(instance)
print(trace)
def check_trace(trace):
    import execjs
    with open('./jdlogin/demo.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)
    result = ctx.call('getbparms', trace)
    time.sleep(6)
    contexts = requests.get(
        'https://seq.jd.com/jseqf.html?bizId=passport_jd_com_login_pc&platform=js&version=1', headers=headers).text
    session_id = re.findall(r'_jdtdmap_sessionId=\"(.+?)\"', contexts)[0]
    print(session_id)
    print(result)
    params_a = {
        'd': result,
        'c': challenge,
        'w': '242',
        'appId': '1604ebb2287',
        'scene': 'login',
        'product': 'click-bind-suspend',
        'e': 'FHWFGUXTWJQDJ7VQMTQK243QCO43XEC5CRGLGTKMVTAV7GWKCPSTIEGSFTX2WRFTUSGB4DUXDFINJJWXQW7IYCPHMU',
        'j': '',
        's': session_id,
        'o': '18566662525',
        'o1': '0',
        'u': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F',
        'lang': 'zh_CN',
        'callback': 'jsonp_022378571588311447',
    }

    response = requests.get('https://iv.jd.com/slide/s.html',
                            params=params_a,  headers=headers).text
    print(response)
    # get validate 
    if 'validate' in response:
        validate = re.findall(r'"validate"\:"(.+?)"', response)[0]
    else:
        validate = ''
    print(validate)
    return validate
check_trace(trace)


# https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F 正则匹配一些数据


