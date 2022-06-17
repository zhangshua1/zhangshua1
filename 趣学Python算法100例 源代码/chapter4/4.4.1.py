#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/15 2:17
# @desc: 最大公约数

if __name__ == "__main__":
    print("请输入两个整数")
    m = int(input("m = "))
    n = int(input("n = "))
    # 比较两个数的大小，进行交换
    if m < n:
        temp = n
        n = m
        m = temp

    for i in range(1, n):
        if m % i == 0 and n % i == 0:
            k = i   # 将当前情况下的最大公约数存储在k中
    print("%d 和 %d 的最大公约数是：%d" %(m, n, k))