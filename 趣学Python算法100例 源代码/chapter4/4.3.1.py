#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/17 2:19
# @desc: 多项式之和

if __name__ == "__main__":
    s = 0  # s记录多项式的和
    n = int(input("请输入一个整数n: "))
    t = 1
    for i in range(1, n+1):  # i<=n, i控制对应项数
        t = t*1/i  #将分式的值赋值给变量t
        s = s + t
    print("%f" %s)