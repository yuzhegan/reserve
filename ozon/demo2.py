# encoding='utf-8

# @Time: 2023-12-30
# @File: %
#!/usr/bin/env
from icecream import ic
import time
from curl_cffi import requests
from lxml import etree
import os
import json
from parseData import ParseData
from parseData import *


class Ozon_Spider:
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
                                impersonate="chrome110", headers=self.headers)
        cookies = response.cookies
        print(cookies)
        return cookies

    def searchResultsV2(self, cookies, searh_text, page):
        params = {
            # 'from_global': 'true',
            'page': page,
            'text': searh_text,
        }
        response = requests.get('https://www.ozon.ru/search/', params=params,
                                cookies=cookies, headers=self.headers, impersonate="chrome110")
        #write to file
        # with open('ozon.txt', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        html = etree.HTML(response.text)
        data = html.xpath('//div[contains(@id,"state-searchResultsV2")]/@data-state')
        # print(data)
        data = json.loads(data[0])
        # with open('ozon.json', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(data, indent=4, ensure_ascii=False))
        return data



if __name__ == '__main__':
    search_text = 'мыльная бабочка'
    ozon = Ozon_Spider()
    cookies = ozon.Get_cookies()
    writer = DataWriter('data.csv')
    str_today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    for page in range(1, 8):
        # page = 1
        time.sleep(1)
        data = ozon.searchResultsV2(cookies, search_text, page)
        print(len(data['items']))
        datas = ParseData(data)
        datas.parseData(writer, search_text, str_today, page)
    writer.close()


    

