#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/16 1:22
# @desc: 最小公倍数

if __name__ == "__main__":
    print("请输入两个整数")
    m = int(input("m = "))
    n = int(input("n = "))
    if m < n:   # 比较两个数的大小，使得m中存储大数，n中存储小数
        temp = m
        m = n
        n = temp
    i = m
    while i > 0:   # 从大数开始寻找满足条件的自然数
        if i % m == 0 and i % n == 0:
            # 输出满足条件的自然数并结束循环
            print("%d 和 %d 的最小公倍数为：%d" %(m, n, i))
            break
        i += 1
