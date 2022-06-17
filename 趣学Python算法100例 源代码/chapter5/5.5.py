#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/20 23:59
# @desc: 哥德巴赫猜想

import math

# 判断是否为素数
def fun(n):
    if n == 2:
        return 1   # n是2,返回1
    if n % 2 == 0:
        return 0    # n是偶数，不是素数，返回0

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return 0   # n是奇数，不是素数，返回0
        i += 2
    return 1  # n是除2以外的素数返回1

# 验证哥德巴赫猜想
def guess(n):
    ok = 0  # 进入循环前先置标志位
    i = 2
    while i <= (n // 2):
        if fun(i):
            if fun(n - i):
                print("%d  %d\n" % (i, n - i))  # i和n-i都是素数，则打印
                ok = 1
        if i != 2:
            i += 1
        if ok == 1:
            break  # 已打印出所需要的输出结果，跳出循环
        i += 1

if __name__ == "__main__":
    while True:    # 循环输入
       n = int(input())
       guess(n)   # 调用方法验证哥德巴赫猜想

