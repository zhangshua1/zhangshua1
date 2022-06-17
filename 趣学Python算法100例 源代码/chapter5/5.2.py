#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/22 11:05
# @desc: 回文素数

# 判断参数n是否为素数
def fun(n):
    for i in range(2, (n-1)//2):
        if n % i == 0:   # 偶数不是素数
            return 0
    return 1  # 返回1是素数


if __name__=="__main__":
    print("1000以内的回文素数：")
    for i in range(0, 9+1):  # 穷举第一位
        for j in  range(0, 9+1): # 穷举第二位
            for k in range(0, 9+1): # 穷举第三位
                n = i * 100 + j * 10 + k  # 计算组成的整数
                m = i + j * 10 + k * 100 # 计算对应的反序数
                if i == 0 and j == 0:  # 处理整数的前两位为0的情况
                    m = m // 100
                elif i == 0:  # 处理整数的第一位为0的情况
                    m = m // 10
                if n > 10 and n == m and fun(n):  # 若大于10且为回文数，则输出
                    print("%d\t" %n, end="")
