# encoding='utf-8

# @Time: 2024-01-04
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import polars as pl

# 读取文件


def read_file():
    # 读取文件
    df = pl.read_excel('./tianwentai/setttings.xlsx')
    # 将id, sex phone 转换为字符串
    df = df.with_columns([pl.col('id').cast(pl.Utf8),
                          pl.col('sex').cast(pl.Utf8),
                          pl.col('phone').cast(pl.Utf8),
                          ])

    # 取出空行
    df = df.filter(pl.col("name").is_not_null()).sort(["week", 'pmAm'])
    # 筛选出“选票”列中的“是”
    df = df.filter(pl.col('starts') == "YES")
    # ic(df)
    return df

# 创建随行成人


def create_flower_data(yupiao, df, week, pmAm):
    # 表示有多少个余票, 最多只能选3个随行 + 1个本人, 最多只能选4个
    # 选出星期几 上午还是下午的票
    df = df.filter((pl.col('week') == week) & (pl.col('pmAm') == pmAm))

    if 1 < yupiao:
        # 选出df中的数据
        flower_df = df[0:yupiao]
        if len(flower_df) > 4:
            flower_df = flower_df[0:4]

    elif yupiao == 1:
        flower_df = df[0:1]
    else:
        flower_df = df[0:0]

    ic(flower_df)
    return flower_df


# if __name__ == '__main__':
    # df = read_file()
    # create_flower_data(5, df, '星期三', '下午')
