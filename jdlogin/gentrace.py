# encoding='utf-8
# @Time: 2023-10-24
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import random
import time
def get_trace(distance):
    """
    生成轨迹
    :param distance:
    :return:
    """
    back = random.randint(2, 6)
    distance += back
    base_x = 313
    base_y = 400
    # 初速度
    v = 0
    # 位移/轨迹列表，列表内的一个元素代表0.02s的位移
    tracks_list = []
    # 当前的位移
    current = 0
    while current < distance - 13:
        # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
        a = random.randint(10000, 12000)  # 加速运动
        # 初速度
        v0 = v
        t = random.randint(9, 18)
        s = v0 * t / 1000 + 0.5 * a * ((t / 1000) ** 2)
        # 当前的位置
        current += s
        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t / 1000
        # 添加到轨迹列表
        if current < distance:
            tracks_list.append(round(current))
    # 减速慢慢滑
    if round(current) < distance:
        for i in range(round(current) + 1, distance + 1):
            tracks_list.append(i)
    else:
        for i in range(tracks_list[-1] + 1, distance + 1):
            tracks_list.append(i)
    # 回退
    for _ in range(back):
        current -= 1
        tracks_list.append(round(current))
    tracks_list.append(round(current) - 1)
    if tracks_list[-1] != distance - back:
        tracks_list.append(distance - back)
    # 生成时间戳列表
    timestamp = int(time.time() * 1000)
    timestamp_list = [timestamp]
    time.sleep(random.uniform(0.5, 1.5))
    for i in range(1, len(tracks_list)):
        t = random.randint(11, 18)
        timestamp += t
        timestamp_list.append(timestamp)
        i += 1
    y_list = []
    for j in range(len(tracks_list)):
        y = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
        y_list.append(y)
        j += 1
    trace = [[str(base_x), str(base_y), timestamp_list[0]]]
    x_offset = random.randint(1, 5)
    y_offset = random.randint(20, 30)
    for index, x in enumerate(tracks_list):
        trace.append([str(base_x + x_offset + x), str(base_y + y_offset + y_list[index]), timestamp_list[index]])
    return trace
 
# if __name__ == '__main__':
#     ic(get_trace(100))
