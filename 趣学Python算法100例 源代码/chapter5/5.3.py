#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/22 11:42
# @desc: 孪生素数


import math

# 判断n是否为素数
def prime(n):
    k = math.sqrt(n) + 1
    i = 2
    while i <= k:
        if n % i == 0:
            return 0  # n能被j整除，不是素数，返回0
        i += 1
    return 1 # n是素数，返回1


if __name__=="__main__":
    count = 0 # 计数器
    print("3到1000之间的孪生素数：")
    for i in range(3, 1000):
        if prime(i) and prime(i+2):
            print("(%-3d, %3d)  " %(i, i+2), end="")
            count += 1
            if count % 5 == 0:  # 每5个数换一行
                print()
    print("\n1000以内的孪生素数共有%d对" %count)
