#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/22 10:41
# @desc: 可逆素数

import math

# 判断素数
def fun(n):
    if n <= 1:
        return 0;  # n<1时显然不是素数，故返回0
    if n == 2:
        return 1  # n=2，是素数，返回1
    if n % 2 == 0:
        return 0  # n是偶数，不是素数，返回0
    for i in range(3, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0  # n是奇数，不是素数，返回0
        i += 2
    return 1   # n是除2以外的素数返回1

if __name__=="__main__":
    count = 0 # 计数器
    # 穷举法
    for a in range(1, 9+1):  # 千位
        for b in range(0, 9+1):  # 百位
            for c in range(0, 9+1):  # 十位
                for d in range(1, 9+1):  # 个位
                    if fun(a*1000+b*100+c*10+d):  # 判断4位整数是否为素数
                        if fun(a+b*10+c*100+d*1000): # 判断4位逆序的整数是否为素数
                            if count % 10 == 0:  # 每十个数就换行
                                print()
                            print("%d   " %(a*1000+b*100+c*10+d), end="")
                            count += 1
    print("\n4位可逆素数共有%d个" %count)




