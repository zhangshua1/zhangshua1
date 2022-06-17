#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/22 2:10
# @desc: 要发就发

import math

# 判断素数
def fun(i):
    if i <= 1:
        return 0;  # n<1时显然不是素数，故返回0
    if i == 2:
        return 1  # n=2，是素数，返回1
    if i % 2 == 0:
        return 0  # n是偶数，不是素数，返回0
    for j in range(3, int(math.sqrt(i) + 1)):
        if i % j == 0:
            return 0  # n是奇数，不是素数，返回0
        j += 2
    return 1   # n是除2以外的素数返回1


if __name__ == "__main__":
    count = 0  # 计数器
    print("列出第一行中差值为1989的所有素数组合: ")
    j = 0
    i = 3
    number = [0]*320
    while i <= 1993:  # 求出不超过1993的全部素数
        if fun(i):
            j = j+1
            number[j] = i
        i += 2
    j = j - 1
    while number[j] > 1898:  # 从最大的素数开始向1898搜索
        # 循环查找满足条件的素数
        i = 0
        while number[j]-number[i] > 1898:
            i += 1
        if number[j] - number[i] == 1898:  # 若两个素数的差为1898，则输出
            count += 1
            print("(%d). %3d,  %d" %(count, number[i], number[j]))
        j -= 1


