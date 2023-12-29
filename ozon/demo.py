# encoding='utf-8
# @Time: 2021-12-18
# @File: %
#!/usr/bin/env
from icecream import ic
import requests
cookies = {
    'cf_clearance': 'jtSyDNo3Ihi8YfZYO6U1aeXjP6m9SkqLbNnX96Gq64w-1703843072-0-2-d314c768.58b432a6.bb187e86-250.2.1703843072',
    'abt_data': 'cf9199db5eaae28c35d1031ac6d1fe1b:7087f615938e17b348f6eb0d92968696c69dc5cb0b79e95eea616774a584b67ad028a6fa45cafc12867f85dfbd9757bc6ebd970822890f2f40bad212d768275d9b06d945032fc3738e5fa706701eb9ccd597e76b602b2689b138c5cc888e9a11a26861fda881ac2ec66978ae848cdf8d42b1445db724ca0463d460bc65119b2a4d31e2fa7ceac328245e2c56668e622f67dcd5c9857ed4cefe3caf7f99029b0757a0540b185f42773efa1f9fe15cb9c90e4555c9df4ef2f97b18ec9e1ea2acff',
}
headers = {
    'authority': 'www.ozon.ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'service-worker-navigation-preload': 'true',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.ozon.ru/',
    'accept-language': 'zh-CN,zh;q=0.9',
}
params = {
    # 'from_global': 'true',
    'page': '3',
    'text': 'мыльная бабочка',
    # 'tf_state': 'DrFTmxshjP1wx9S8WD0J4GMOXOnart-Pdj5ntgL_E-9sc1g=',
}
response = requests.get('https://www.ozon.ru/search/', params=params, cookies=cookies, headers=headers)
# write to file
with open('ozon.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
