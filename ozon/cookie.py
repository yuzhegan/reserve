# encoding='utf-8
# @Time: 2023-12-29
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
headers = {
    'authority': 'www.ozon.ru',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '69332',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.ozon.ru',
    'pragma': 'no-cache',
    'referer': 'https://www.ozon.ru/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
session = requests.Session()
session.headers.update(headers)

data = '{"events":[{"event":{"attributes":{"platform":"site","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36","screenResolutionX":1920,"screenResolutionY":1080,"namespace":"bx","appVersion":"TSDK:2.3.3"},"user":{"isBot":false,"marketplaceId":1},"page":{"current":"home","title":"OZON — интернет-магазин. Миллионы товаров по выгодным ценам","number":2,"currentUrl":"https://www.ozon.ru/","referralUrl":"https://www.ozon.ru/","previous":"home","pageViewId":"4629e318-dcb3-49b1-0826-6c7efe74e9aa","previousPageViewId":"ffbcfd70-2eb0-48bd-60f6-d175c31f59a3"},"viewTime":44477,"scrollDepth":0,"actionType":"page_close","object":{"type":"page"},"timestamp":"2023-12-29 19:37:35 +0800","pageTimestamp":"2023-12-29 19:36:51 +0800","uuid":"d09a2dde-7a8a-47db-8845-8dd6a6d3b027"}}]}'.encode()
response = session.post('https://xapi.ozon.ru/dlte/multi', data=data)
ic("=================")
ic(response.cookies)

Secure_access_token = response.cookies['__Secure-access-token']
Secure_refresh_token = response.cookies['__Secure-refresh-token']
ic(Secure_access_token)
ic(Secure_refresh_token)

# %%
response = session.post('https://www.ozon.ru/abt/result')
cf_bm = response.cookies['__cf_bm']
ic("=================")
ic(cf_bm)


cookies = {
    '__cf_bm': cf_bm,
    '__Secure-access-token': Secure_access_token,
    '__Secure-refresh-token': Secure_refresh_token,
    '__Secure-ab-group': '60',
    '__Secure-user-id': '0',
}

ic("=================")
response = session.post('https://www.ozon.ru/favicon.ico', cookies=cookies)
ic(response.status_code)
ic(response.cookies)
