#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/11 22:46
# @desc: 水仙花数

if __name__ == '__main__':
    print("result is: ")
    for n in range(100, 1000):  # 整数的取值范围
        hun = n // 100  # 百位
        ten = (n - hun * 100) // 10  # 十位
        ind = n % 10  # 个位
        m = hun*hun*hun + ten*ten*ten + ind*ind*ind # 求和
        if n == m:  # 各位上的立方和是否与原数n相等
            print("%d \t" %n, end=" ")

