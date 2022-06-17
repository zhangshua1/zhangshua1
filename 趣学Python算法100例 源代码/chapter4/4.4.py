#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/14 1:44
# @desc: 最大公约数

if __name__ == "__main__":
    print("请输入两个整数")
    m = int(input("m = "))
    n = int(input("n = "))
    if m < n:   # 比较大小，使得m中存储大数，n中存储小数
        # 交换m和n的值
        temp = m
        m = n
        n = temp

    i = n  # 按照从大到小的顺序寻找满足条件的自然数
    while i > 0:
        if m % i == 0 and n % i == 0:
            # 输出满足条件的自然数并结束循环
            print("%d 和 %d 的最大公约数是： %d" %(m, n, i))
            break
        i -= 1
