#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/15 2:22
# @desc: 最大公约数——辗转相除法

if __name__ == "__main__":
    print("请输入两个整数")
    m = int(input("m = "))  # m存储较大数
    n = int(input("n = "))  # n存储较小数
    print("%d 和 %d 的最大公约数是： " % (m, n), end="")
    # 比较两个数的大小，进行交换，使得m是最大数，n是最小数
    if m < n:
        temp = n
        n = m
        m = temp
    b = m % n   # b存储m 和 n取模得到的余数
    while b != 0:
        m = n  # 原来的小数作为下次运算时的大数
        n = b  # 将上一次的余数作为下次相除时的小数
        b = m % n
    print("%d" %n)
