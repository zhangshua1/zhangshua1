#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/17 2:07
# @desc: 多项式之和

if __name__ == "__main__":
    n = int(input("请输入一个整数n: "))
    s = 0  # s记录多项式的和
    i = 1
    while i <= n:  # i控制对应项数
        t = 1  # t记录每一项分式的分母，每次循环之前给t赋初值
        j = 1
        while j <= i:
            t = t * j  # 每一项的阶乘
            j += 1
        s = s + 1/t
        i += 1
    print("%f" %s)

