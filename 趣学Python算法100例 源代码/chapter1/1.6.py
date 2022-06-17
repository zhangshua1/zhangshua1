#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/5/30 1:09
# @desc: 打鱼还是晒网

import datetime

#计算输入的年月日与1990年1月1日相差的天数
def differ_days(year, month, day):
    d1 = datetime.datetime(1990, 1, 1)
    d2 = datetime.datetime(year, month, day)
    differ_days = (d2 - d1).days + 1
    print("%d年%d月%d日与1990年1月1日相差 %d 天" %(year, month, day, differ_days))
    return differ_days


#利用相差的天数判断是打鱼还是晒网
def fish_or_sun(day):
    result = day % 5
    if 0 < result < 4:
        print("今天打鱼")
    else:
        print("今天晒网")


if __name__=="__main__":
    print("请输入一个日期，包括年，月，日：")
    while True:
        year = int(input("请输入年份："))
        month = int(input("请输入月份："))
        day = int(input("请输入日期："))
        days = differ_days(year, month, day)
        fish_or_sun(days)
        print()

