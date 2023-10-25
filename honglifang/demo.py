# encoding='utf-8

# @Time: 2023-10-24
# @File: %
#!/usr/bin/env
# %%
import hashlib
from icecream import ic
import os
import requests
import time

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://webchat.sz-redcube.com',
    'Pragma': 'no-cache',
    'Referer': 'http://webchat.sz-redcube.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue',
}

cliendId = 'f7ce1e1a-3923-9054-eb2f-c5cea952c9b8'
signKey = 'srAO407hOx04NrP1g3rDoIWzaTO4fda7F'
# md5加密


def hex_md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

# 登陆


def login():
    stime = int(time.time() * 1000)
    timestamp = str(stime)
    sign = hex_md5(cliendId + timestamp + signKey).upper()
    # sign = hex_md5('f7ce1e1a-3923-9054-eb2f-c5cea952c9b81698156950932srAO407hOx04NrP1g3rDoIWzaTO4fda7F').upper()
    print(sign)

    json_data = {
        'deviceId': cliendId,
        'sendTime': str(stime),
        'sign': sign,
        'username': '15985926948',
        'password': 'aaa4343',
        # 'username': '15083861116',
        # 'password': 'zt2580',
        'openId': 'o80mt0ffmsdwmqrfgqH-I9j2kN44',
    }

    response = requests.post('http://webchatapi.sz-redcube.com/login/checkUser',
                             headers=headers, json=json_data, verify=False).json()
    print("登陆信息===》》", response)
    return response

# 获取所有活动数据


def getAllActivity(userId, accessToken, chooseTime):
    timestamp = str(int(time.time() * 1000))
    sign = hex_md5(cliendId + timestamp + signKey).upper()
    json_data = {
        'deviceId': cliendId,
        'sendTime': timestamp,
        'sign': sign,
        'userId': userId,
        'accessToken': accessToken,
        'orderBy': ' activity_start_time desc ',
        'pageNumb': 1,
        'pageSize': 50,
        'activityType': '66',
        # 'activityStartTime': '2023-10-28',
        'activityStartTime': chooseTime,
    }

    response = requests.post(
        'http://webchatapi.sz-redcube.com/reservation/activity/getAllActivitiesNew',
        headers=headers,
        json=json_data,
        verify=False,
    ).json()
    print("所有活动数据==》》", response)
    return response

# getUserInfo


def getUserInfo(userId, accessToken):
    timestamp = str(int(time.time() * 1000))
    sign = hex_md5(cliendId + timestamp + signKey).upper()
    json_data = {
        'deviceId': cliendId,
        'sendTime': timestamp,
        'sign': sign,
        'userId': userid,
        'accessToken': accessToken,
    }

    response = requests.post('http://webchatapi.sz-redcube.com/user/user/getUserInfo',
                             headers=headers, json=json_data, verify=False).json()
    print("UserInfo是==》》", response)
    return response
# getContantList


def getContantList(userid, accessToken):
    timestamp = str(int(time.time() * 1000))
    sign = hex_md5(cliendId + timestamp + signKey).upper()
    json_data = {
        'deviceId': cliendId,
        'sendTime': timestamp,
        'sign': sign,
        'userId': userid,
        'accessToken': accessToken,
    }

    response = requests.post(
        'http://webchatapi.sz-redcube.com/user/contact/contactList',
        headers=headers,
        json=json_data,
        verify=False,
    ).json()
    print("contactList用户信息==》》", response)
    return response

# 立即预约


def doReservationNew(userid, accessToken, openId, activtyId, activtyDateId, activtyAddressZh, activityType):
    # activtyId = '132' # 龙岗科技管
    # activtyId = '12' #"科技馆2F(单次入馆无需重复预约科技馆)" 上午 IDea乐园
    # activtyId = '11' #"科技馆2F(单次入馆无需重复预约科技馆)" 下午 IDea乐园

    timestamp = str(int(time.time() * 1000))
    sign = hex_md5(cliendId + timestamp + signKey).upper()
    json_data = {
        'deviceId': cliendId,
        'sendTime': timestamp,
        'sign': sign,
        'userId': userid,
        'accessToken': accessToken,
        'openId': openId,
        # 'activityId': '132', #龙岗科技管
        'activityId': activtyId,
        'activityModifyUser': userid,
        'activityType': activityType,  # 预约人数?
        'activityMaxPeople': '5250',
        'activityDateId': activtyDateId,
        'activityAddressZh': activtyAddressZh,  # 预约人ID,可以多个
        'paymentStatus': 3,
        'baomingActivityType': 66,
    }

    '''json_data = {
        'deviceId': 'f7ce1e1a-3923-9054-eb2f-c5cea952c9b8',
        'sendTime': 1698239168086,
        'sign': 'EF9BBD70350B0B4D235EBE8F0D55D9D5',
        'userId': 1290759,
        'accessToken': 5512963501744128,
        'openId': 'o80mt0ffmsdwmqrfgqH-I9j2kN44',
        'activityId': '132',
        'activityModifyUser': 1290759,
        'activityType': 3,
        'activityMaxPeople': '5407',
        'activityDateId': '16641',
        'activityAddressZh': '2780877,2780878,2780879',
        'paymentStatus': 3,
        'baomingActivityType': 66,
    }'''

    response = requests.post(
        'http://webchatapi.sz-redcube.com/reservation/activity/doReservationNew',
        headers=headers,
        json=json_data,
        verify=False,
    )
    print("立即预约==》》", response.status_code)
    print(response.json())
    print("done")
# %%


if __name__ == '__main__':
    # %%
    response = login()
    # %%
    accessToken = response['data']['accessToken']
    userid = response['data']['userId']
    openId = response['data']['openId']
    # %%
    res = getAllActivity(userid, accessToken, '2023-11-01')
    # %%
    # idea乐园上午场
    lists = res['data']['list']
    for list in lists:
        if "下午" in list['activityTitleZh']:
            activtyId = list['activityId']
            activityDataId = list['id']


    # %%
    getUserInfo(userid, accessToken)
    # %%
    resp = getContantList(userid, accessToken)
    # %%
    activityType = len(resp['data']['data'])
    activityAddressZhList = []
    for data in resp['data']['data']:
        activityAddressZhList.append(str(data['contactId']))
        
    activityAddressZh = ','.join(activityAddressZhList)
    print(activityAddressZh)


    # %%
    print(activtyId, activityDataId, activityAddressZh, activityType)
    # %%
    doReservationNew(userid, accessToken, openId, activtyId, activityDataId, activityAddressZh, activityType)


'''
# 预约
json_data = {
    'deviceId': 'f7ce1e1a-3923-9054-eb2f-c5cea952c9b8',
    'sendTime': 1698160806984,
    'sign': '29416F6D8AF21D020F22380518778982',
    'userId': 1290759,
    'accessToken': 5511690075054080,
    'openId': 'o80mt0ffmsdwmqrfgqH-I9j2kN44',
    'activityId': '132',
    'activityModifyUser': 1290759,
    'activityType': 1,
    'activityMaxPeople': '6866',
    'activityDateId': '16639',
    'activityAddressZh': '2780878',
    'paymentStatus': 3,
    'baomingActivityType': 66,
}

response = requests.post(
    'http://webchatapi.sz-redcube.com/reservation/activity/doReservationNew',
    headers=headers,
    json=json_data,
    verify=False,
)

# 预约
json_data = {
    'deviceId': 'f7ce1e1a-3923-9054-eb2f-c5cea952c9b8',
    'sendTime': 1698158445326,
    'sign': 'AADFC573E6E110DEC15B730EABB8D798',
    'userId': 1290759,
    'accessToken': 5511653184823296,
    'openId': 'o80mt0ffmsdwmqrfgqH-I9j2kN44',
    'activityId': '132',   # 活动id 龙岗区科技馆
    'activityModifyUser': 1290759,
    'activityType': 1,
    # 'activityMaxPeople': '6868', #最大可报名人数
    'activityDateId': '16639',  # 日期id
    'activityAddressZh': '2780877',
    'paymentStatus': 3,
    'baomingActivityType': 66,
}

response = requests.post(
    'http://webchatapi.sz-redcube.com/reservation/activity/doReservationNew',
    headers=headers,
    json=json_data,
    verify=False,
)
'''
