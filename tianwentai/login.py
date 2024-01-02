# encoding='utf-8

# @Time: 2024-01-01
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import re

# gen code 

# import requests
#
#
# headers = {
#     "authority": "open.weixin.qq.com",
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "cache-control": "no-cache",
#     "content-type": "application/x-www-form-urlencoded",
#     "origin": "https://open.weixin.qq.com",
#     "pragma": "no-cache",
#     "referer": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx6afdd1b805932524&redirect_uri=https%3A%2F%2Fweather.121.com.cn%2Fsztwt%2F%23%2Fgr&response_type=code&scope=snsapi_userinfo&state=3&uin=MjQyMTEwMDEwNQ%3D%3D&key=47b3874b26cb62d2b1a2b6949d118e44ca966702b00931cc7f15cba7336ab503963c597c2dcc64ae9ff378274f93ddca2e0ddaa6236ae8d72687a6e4a94e61a00cce7e86b3739aed11f53ad8cee0d1426b059220ec16631dd3d3dbc7a27eb694d8199b19f2c069940a97dce0184dc1646a8dd9b56d9880dbc91a8105fc939fa8&version=6309071d&exportkey=n_ChQIAhIQf5ff5M%2FQW3XbUsZqb0dJVhLJAQIE97dBBAEAAAAAAIXICm6n%2BNcAAAAOpnltbLcz9gKNyK89dVj07K%2B1XQRieRNow4fsOpemSmoJ5S1q4MBuKfYbNHGeoGZnx06jJS6jq2K9J9okPj6%2F9hlKp0UA6%2BTovXaRIqazApIsDJRGeDuUf5b9UOLSiorQX3a%2F5OXGaZnb1VpvFnLplQJTrlHx%2BJOAHUq8%2Fw8PqPL67qPz%2BtOpAcsLr%2BHR2grLt5ci%2FHcSy637KlBXctU1%2FYoPWkvTnlYXByAarONwBM5nwQ%3D%3D&pass_ticket=QNH%2BedyfUFDzLGLwsvylVtfPVA2Pu6NpLHJqescZODQdfQJtcMCidfA73RNQwcsuVje50PmkGiUnESaWrCUbEg%3D%3D&wx_header=0",
#     "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Linux\"",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# url = "https://open.weixin.qq.com/connect/oauth2/authorize_reply"
# data = {
#     "snsapi_userinfo": "on",
#     "allow": "同意",
#     "uuid": "011YPhKa13ukFa1s",
#     "uin": "MjQyMTEwMDEwNQ==",
#     "key": "47b3874b26cb62d2b1a2b6949d118e44ca966702b00931cc7f15cba7336ab503963c597c2dcc64ae9ff378274f93ddca2e0ddaa6236ae8d72687a6e4a94e61a00cce7e86b3739aed11f53ad8cee0d1426b059220ec16631dd3d3dbc7a27eb694d8199b19f2c069940a97dce0184dc1646a8dd9b56d9880dbc91a8105fc939fa8",
#     "pass_ticket": "QNH+edyfUFDzLGLwsvylVtfPVA2Pu6NpLHJqescZODQdfQJtcMCidfA73RNQwcsuVje50PmkGiUnESaWrCUbEg==",
#     "version": "6309071d"
# }
# response = requests.post(url, headers=headers, data=data)
#
# print(response.text)
# print(response)
# print(response.url)




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
    "code": "0915H70w3qKNZ132H01w3mMm1k45H70P",
    "redirect_uri": "https://weather.121.com.cn/sztwt/#/gr"
}
response = requests.get(url, headers=headers, params=params)

# print(response.text)
# print(response)
# print 当前url
print("当前url",response.url)
