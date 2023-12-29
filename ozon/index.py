# encoding='utf-8
# @Time: 2023-12-13
# @File: %
#!/usr/bin/env
from icecream import ic
import requests

cookies = {
    '__Secure-access-token': '3.0.SFIXxzN2QcabwjSxKojv1g.56.l8cMBQAAAABljqXDDTqOnaN3ZWKgAICQoA..20231229125603.jHoLJblXRWZqctd76SvBWqtS7z2MVa_kM-mQ_gd7MEo',
    '__Secure-refresh-token': '3.0.SFIXxzN2QcabwjSxKojv1g.56.l8cMBQAAAABljqXDDTqOnaN3ZWKgAICQoA..20231229125603.OUdDObiRYD0PuJsFfvWTlauf6F6SwDUlmB04-fwmJCY',
    '__Secure-ab-group': '56',
    '__Secure-user-id': '0',
    'abt_data': '0e3fa5084d50e032dfd57a77dc511a61:d1811f609545f80d02a8b49f734b387f7dd076b3762f42117d46824bca7928f127d67eb2b10994525feae3ff1ee93c19d33f8bbd1fd3df1650c85ed21d7e993385533e75b839be69f851acc0f02ae14767aa62dbd69a28cce9f13dd71ed65370d4751ae29374a34705aa5cf7181ea6d1d9eb48e8f63d32ad9ef4d8bf64fac816282f31214f8596db836feb31142f604c0d50a8c161dfa3db77295c90ec8ea653',
    'cf_clearance': 'BTanAMGTkYACFDvwOeSpDlLr.fed_nfwPEVTyVzO2n4-1703847361-0-2-d314c768.58b432a6.bb187e86-250.0.0',
    '__cf_bm': 'F.j65AwwL_W5DvxcGMEkxBCaDnlBNfCcVW2AhwncAec-1703847401-1-ATHjdtaiQhDpU77n4ZZBs3GtP5izrk0sU9MaXQSQGvusZ8mShaCZwCWYs1DF0ozTI7JMwTeQx8ek+f1SiEpb9+Q=',
}
headers = {
    'authority': 'www.ozon.ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'service-worker-navigation-preload': 'true',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9',
}
response = requests.get('https://www.ozon.ru/', cookies=cookies, headers=headers)
# write to file
with open('indx.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
