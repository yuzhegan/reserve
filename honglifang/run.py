# encoding='utf-8

# @Time: 2023-10-26
# @File: %
#!/usr/bin/env
from icecream import ic
import os


from multiprocessing import Process
import subprocess

# script_path = os.path.join(os.path.dirname(__file__), 'demo2.py')
def run_script(arguments):
    # 在这里执行脚本的代码，使用传递的参数param
    script_path = './honglifang/demo.py'
    # arguments = ['-u', 'yuzhe', '-p', '123456', '-d', '2024-11-03', '-a', '下午场一']

    subprocess.call(['python', script_path] + arguments)



# # 参数列表
params1 = ['-u', '15083861116', '-p', 'zt2580', '-d', '2023-11-02', '-a', '下午场一']
params2 = ['-u', '15985926948', '-p', 'aaa4343', '-d', '2023-11-02', '-a', '下午场二']

params = [params1, params2]
# print(params)
#
# 创建进程列表
processes = []

# 创建并启动进程
for param in params:
    p = Process(target=run_script, args=(param,))
    p.start()
    processes.append(p)

# 等待所有进程完成
for p in processes:
    p.join()
