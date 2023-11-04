# encoding='utf-8

# @Time: 2023-10-26
# @File: %
#!/usr/bin/env
import time
from Proxy_JiGuang import Proxy_JiGuang
from icecream import ic
import os
import random


from multiprocessing import Process
import subprocess

# script_path = os.path.join(os.path.dirname(__file__), 'demo2.py')


def run_script(arguments):
    # 在这里执行脚本的代码，使用传递的参数param
    script_path = './honglifang/demo.py'
    # arguments = ['-u', 'yuzhe', '-p', '123456', '-d', '2024-11-03', '-a', '下午场一']

    subprocess.call(['python', script_path] + arguments)


# # 参数列表
# params1 = ['-u', '19842655890', '-p', 'hlf137', '-d', '2023-11-04', '-a', '上午'] # 两个一小
# params2 = ['-u', '18466241111', '-p', 'hlf138', '-d', '2023-11-04', '-a', '下午场一'] # 两个一小
# params3 = ['-u', '18682851861', '-p', 'kjg3578', '-d', '2023-11-04', '-a', '下午场二'] # 两个一小
# params4 = ['-u', '15107042854', '-p', '459000', '-d', '2023-11-04', '-a', '上午'] # 两个2小
# params5 = ['-u', '18720600577', '-p', 'hlf4210', '-d', '2023-11-04', '-a', '下午场一'] # 两个2小
# params6 = ['-u', '18974573951', '-p', 'hlf123', '-d', '2023-11-04', '-a', '下午场二']  # 两个2小
# params7 = ['-u', '18172856581', '-p', 'wq6666', '-d', '2023-11-04', '-a', '晚上']  # 两个2小
params1 = ['-u', '15707974367', '-p', 'ccc123','-d', '2023-11-11', '-a', '上午']  # 两个一小
params2 = ['-u', '18870011708', '-p', 'sb123456','-d', '2023-11-11', '-a', '下午场一']  # 两个一小
params3 = ['-u', '18146700772', '-p', '112580','-d', '2023-11-11', '-a', '下午场一']  # 两个一小
params4 = ['-u', '18126152622', '-p', '221212','-d', '2023-11-11', '-a', '下午场二']  # 两个2小
params5 = ['-u', '15907986641', '-p', '451234','-d', '2023-11-11', '-a', '上午']  # 两个2小
params6 = ['-u', '18466238170', '-p', 'hlf127','-d', '2023-11-11', '-a', '下午场二']  # 两个2小
# params6 = ['-u', '18974573951', '-p', 'hlf123', '-d', '2023-11-04', '-a', '下午场二']  # 两个2小
# params7 = ['-u', '18172856581', '-p', 'wq6666', '-d', '2023-11-04', '-a', '晚上']  # 两个2小
# params = [params1, params2]
params = [params1,params2, params3, params4, params5, params6]
# print(params)
#
# 创建进程列表
processes = []



# import ast
# def convert_to_dict(string):
#     try:
#         dictionary = ast.literal_eval(string)
#         if isinstance(dictionary, dict):
#             return dictionary
#         else:
#             raise ValueError('提供的字符串不是一个有效的字典格式。')
#     except SyntaxError:
#         raise ValueError('提供的字符串不是一个有效的字典格式。')
# string = "{'http': 'http://221.229.53.141:6727', 'https': 'https://221.229.53.141:6727'}"
# proxies = convert_to_dict(string)
# print(proxies)


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
# time.sleep(wait_seconds)
proxy = Proxy_JiGuang()
proxy.SetLocalIp2WhiteList()
ips = proxy.GenJG_Proxy_IPs()
ic(ips)


for param in params:
    ip = random.choice(ips)
    proxies = {
        "http": "http://" + str(ip['ip'])+':'+str(ip['port']),
        "https": "https://" + str(ip['ip'])+':'+str(ip['port']),
    }
    # proxies = convert_to_dict(str(proxies))
    param.append('-x')
    param.append(str(proxies))

ic(params)


# 创建并启动进程
for param in params:
    p = Process(target=run_script, args=(param,))
    p.start()
    processes.append(p)

# 等待所有进程完成
for p in processes:
    p.join()
