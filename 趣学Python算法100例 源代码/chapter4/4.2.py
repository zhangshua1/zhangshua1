#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/18 1:12
# @desc: 列出真分数序列——利用辗转相除法

if __name__ == "__main__":
    print("分母为40，分子小于40的最简分数有：")
    n = 0  # 计数器，记录最简分数的个数
    for i in range(1, 40):  # 穷举40以内的全部分子
        num1 = 40   # 分母
        num2 = i # 分子
        # 采用辗转相除法求出分子与分母的最大公约数
        while num2 != 0:
            temp = num1 % num2
            num1 = num2
            num2 = temp
        if num1 == 1: # 若最大公约数为1，则为最简真分数
            n += 1
            print("%2d/40 " %i, end=" ")
            if n % 8 == 0:  # 每8个一行
                print()
