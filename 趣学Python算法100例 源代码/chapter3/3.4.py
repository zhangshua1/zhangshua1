#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/8 23:35
# @desc: 完数

if __name__=="__main__":
    n = int(input("请输入所选范围上限： "))
    i = 2  # 变量 i 控制选定数范围
    while i <= n:
        s = 0  # s记录累加因子之和,保证每次循环时s的初值为0
        j = 1  # j 控制除数范围
        for j in range(i):
            if j != 0 and i % j == 0:  # 判断 j 是不是 i 的因子
                s += j  # 因子和

        if s == i:  # 判断因子之和是否和原数相等
            print("2到%d之间的完数：%d" %(n, i))
        i += 1

