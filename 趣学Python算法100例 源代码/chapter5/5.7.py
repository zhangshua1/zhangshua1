#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/22 12:25 
# @desc: 梅森素数

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
    n = 0
    print("梅森素数：")
    for i in range(2, 20):
        mp = (2 ** i) - 1  # 求梅森数
        if prime(mp):  # 判断mp是否为梅森素数
            n += 1
            print("M(%d) = %d" %(i, mp))  # 若当前mp为梅森素数，则打印， i为指数
    print("2的指数n<20的所有梅森素数有：%d个" %n)

