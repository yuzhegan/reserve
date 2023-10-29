# encoding='utf-8

# @Time: 2023-10-24
# @File: %
#!/usr/bin/env
# %%
import sys
import getopt
import hashlib
from icecream import ic
import os
import requests
import time
import execjs

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
with open('./honglifang/clientid.js', 'r', encoding='utf-8') as f:
    js = f.read()
ctx = execjs.compile(js)
cliendId = ctx.call('guid')
print(cliendId)
# cliendId = 'f7ce1e1a-3923-9054-eb2f-c5cea952c9b8'
signKey = 'srAO407hOx04NrP1g3rDoIWzaTO4fda7F'
# md5加密


def hex_md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

# 登陆


def login(username, password):
    stime = int(time.time() * 1000)
    timestamp = str(stime)
    sign = hex_md5(cliendId + timestamp + signKey).upper()
    # sign = hex_md5('f7ce1e1a-3923-9054-eb2f-c5cea952c9b81698156950932srAO407hOx04NrP1g3rDoIWzaTO4fda7F').upper()
    print(sign)

    json_data = {
        'deviceId': cliendId,
        'sendTime': str(stime),
        'sign': sign,
        'username': username,
        'password': password,
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
    # print("所有活动数据==》》", response)
    return response

# getUserInfo


def getUserInfo(userId, accessToken):
    timestamp = str(int(time.time() * 1000))
    sign = hex_md5(cliendId + timestamp + signKey).upper()
    json_data = {
        'deviceId': cliendId,
        'sendTime': timestamp,
        'sign': sign,
        'userId': userId,
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


def doReservationNew(username, userid, accessToken, openId, activtyId, activtyDateId, activtyAddressZh, activityType):
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
    print(username, "done")
# %%


def seckill_program(username, passwd, dateTime, amopm):
    print("秒杀定时程序已启动！")
    response = login(username, passwd)
    accessToken = response['data']['accessToken']
    userid = response['data']['userId']
    # print("userid==》》", userid)
    openId = response['data']['openId']
    # print("openId==》》", openId)
    res = getAllActivity(userid, accessToken, dateTime)
    # idea乐园上午场
    lists = res['data']['list']
    for list in lists:
        if amopm in list['activityTitleZh']:
            activtyId = list['activityId']
            activityDataId = list['id']

    getUserInfo(userid, accessToken)
    resp = getContantList(userid, accessToken)
    activityType = len(resp['data']['data'])
    activityAddressZhList = []
    for data in resp['data']['data']:
        activityAddressZhList.append(str(data['contactId']))

    activityAddressZh = ','.join(activityAddressZhList)
    # print(activityAddressZh)

    # print(activtyId, activityDataId, activityAddressZh, activityType)
    doReservationNew(username, userid, accessToken, openId, activtyId,
                     activityDataId, activityAddressZh, activityType)
    # 在这里编写你的秒杀定时程序逻辑
    # ...


def main(argv):
    username = ''
    passwd = ''
    dateTime = ''
    amopm = ''

    try:
        opts, args = getopt.getopt(argv[1:], "ha:u:p:d:a", [
                                   "ufile=", "pfile=", "dfile=", "afile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile> <++>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            useage(argv[0])
            sys.exit()
        elif opt in ("-u", "--ufile"):
            username = arg
        elif opt in ("-p", "--pfile"):
            passwd = arg
        elif opt in ("-d", "--dfile"):
            dateTime = arg
        elif opt in ("-a", "--pfile"):
            amopm = arg
        # 获取当前时间
    current_time = time.localtime()
    # 设置目标时间为 10:53:00
    target_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                   16, 00, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
    # 计算需要等待的秒数
    current_timestamp = time.mktime(current_time)
    target_timestamp = time.mktime(target_time)
    wait_seconds = target_timestamp - current_timestamp
    print("等待", wait_seconds, "秒")
    # 等待到目标时间
    time.sleep(wait_seconds)
    # 在目标时间执行秒杀定时程序
    # seckill_program('18682001980', '123456', '2021-09-26', '上午')
    try:
        seckill_program(username, passwd, dateTime, amopm)
        # login(username, passwd)
    except Exception as e:
        print(e)

    # print('输入的文件为：', inputfile)
    # print('输出的文件为：', outputfile)


if __name__ == "__main__":
    main(sys.argv)
    # python demo.py -u "yuzhe" -p "123456" -d "2024-11-03" -a "下午场一"


'''
if __name__ == '__main__':
    # 获取当前时间
    current_time = time.localtime()
    # 设置目标时间为 10:53:00
    target_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 16, 00, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
    # 计算需要等待的秒数
    current_timestamp = time.mktime(current_time)
    target_timestamp = time.mktime(target_time)
    wait_seconds = target_timestamp - current_timestamp
    print("等待", wait_seconds, "秒")
    # 等待到目标时间
    time.sleep(wait_seconds)
    # 在目标时间执行秒杀定时程序
    # seckill_program('18682001980', '123456', '2021-09-26', '上午')
    seckill_program()



# 预约
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
    'activityAddressZh': '2780877', 预约人数
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
