# encoding='utf-8
# @Time: 2024-01-05
# @File: %
#!/usr/bin/env
from icecream import ic
import os
from curl_cffi import requests
class CookiePool:
    def __init__(self):
        self.headers = {
        'authority': 'www.ozon.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    def Get_cookies(self):
        response = requests.get('https://www.ozon.ru/abt/result',
                                impersonate="chrome110", headers=self.headers).cookies
        cookies = response
        # dict_cookies = {}
        # for key, value in cookies.items():
        #     dict_cookies[key] = value
        # return dict_cookies
        return cookies

# if __name__ == '__main__':
#     cookies  = CookiePool().Get_cookies()
#     # 转字典
#     print(cookies)


