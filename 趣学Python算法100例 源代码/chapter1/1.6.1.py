#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/5/31 22:56
# @desc: 打鱼还是晒网

# 判断是否为闰年，是返回1，否返回0
def runYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # 是闰年
        return 1
    else:
        return 0


# 计算指定日期距离1990年1月1日的天数
def countDay(currentDay):
    perMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]  # 每月天数数组*/
    totalDay = 0
    year = 1990
    while year < currentDay['year']:  # 求出指定日期之前的每一年的天数累加和
        if runYear(year) == 1:  # 判断是否为闰年
            totalDay = totalDay + 366
        else:
            totalDay = totalDay + 365

        year += 1

    # 如果为闰年，则二月份为29天
    if runYear(currentDay['year']) == 1:
        perMonth[2] += 1

    i = 0
    while i < currentDay['month']:# 将本年内的天数累加到totalDay中
        totalDay += perMonth[i]
        i += 1

    totalDay += currentDay['day']  # 将本月内的天数累加到totalDay中

    return totalDay


if __name__ == '__main__':
    while True:
        print("please input 指定日期 包括年,月,日 如:1999 1 31")
        year, month, day = [int(i) for i in input().split()]
        # 定义一个日期字典
        today = {'year': year, 'month': month, 'day': day}

        totalDay = countDay(today)  # 求出指定日期距离1990年1月1日的天数
        print("%d年%d月%d日与1990年1月1日相差 %d 天" % (year, month, day, totalDay))

        # 天数 % 5，判断输出打鱼还是晒网
        result = totalDay % 5
        if result > 0 and result < 4:
            print("今天打鱼")
        else:
            print("今天晒网")
