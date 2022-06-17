#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/22 11:27
# @desc: 回文素数

# 判断参数n是否为素数
def fun(n):
    for i in range(2, (n-1)//2):
        if n % i == 0:   # 偶数不是素数
            return 0
    return 1  # 返回1是素数

if __name__=="__main__":
    print("1000以内的回文素数：")
    print("2位回文数是：", 11)
    print("3位回文数是：")
    i = 100
    while i < 1000:
        a = i // 100  # 百位
        b = i % 100 // 10  # 十位
        c = i % 100 % 10
        n = a * 100 + b * 10 + c
        m = a + b * 10 + c * 100
        if n == m and fun(n):
            print("%d\t" %n , end="")

        i += 1