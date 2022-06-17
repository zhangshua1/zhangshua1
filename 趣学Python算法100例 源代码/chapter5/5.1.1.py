#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/22 10:54
# @desc: 孪生素数
# 孪生素数是指：若a为素数，且a+2也是素数，则素数a和a+2称为孪生素数。

import math

# 判断素数
def fun(a):
    if a <= 1:
        return 0;  # n<1时显然不是素数，故返回0
    if a == 2:
        return 1  # n=2，是素数，返回1
    if a % 2 == 0:
        return 0  # n是偶数，不是素数，返回0
    for i in range(3, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return 0  # n是奇数，不是素数，返回0
        i += 2
    return 1   # n是除2以外的素数返回1

if __name__=="__main__":
    print("1000以内的孪生素数：")
    count = 0 # 计数器
    a = 0
    while a <= 1000:
        if fun(a): # 判断 a 是否为素数
            if fun(a+2):  # 判断 a+2 是否为素数
                if count % 5 == 0:  # 每十个数就换行
                    print()
                print("%3d-%3d   " %(a, a+2), end="")
                count += 1
        a += 1
    print("\n1000以内的孪生素数共有%d对" %count)

