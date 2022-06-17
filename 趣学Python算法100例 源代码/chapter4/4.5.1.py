#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/16 1:27
# @desc: 最小公倍数——利用两数的最大公约数求出最小公倍数

if __name__ == "__main__":
    print("请输入两个整数")
    m = int(input("m = "))
    n = int(input("n = "))
    k = m * n  # k存储两数的乘积
    print("%d 和 %d 的最小公倍数为： " %(m, n), end="")
    if m < n:   # 比较两个数的大小，使得m存储大数，n存储小数
        temp = m
        m = n
        n = temp
    b = m % n  # b存储m除以n的余数
    while b != 0:
        m = n   # 原来的小数作为下次运算时的大数
        n = b   # 将上一次的余数作为下次相除时的小数
        b = m % n
    resultNum = k // n   # 两数乘积除以最大公约数即为它们的最小公倍数
    print("%d" %resultNum)

