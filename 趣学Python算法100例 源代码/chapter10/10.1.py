#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/29 23:13
# @desc: 尼科彻斯定理
# 任何一个整数的立方都可以表示成一串连续的奇数的和。

if __name__ == "__main__":
    sum = 0 # sum变量存放奇数的累加和，初值为0
    n = int(input("请输入大于1的n值："))
    if n <= 1:
        print("输入的n值有误")
        exit()
    cube = n * n * n   # cube存放n的立方  也可以写成：cube = n ** 3
    # 外层循环通过累加和来查找奇数序列
    i = 1
    while i < cube:
        # 内层循环通过累加和来查找奇数序列
        j = i
        while j < cube:
            sum += j
            # 找到了奇数序列
            if sum == cube:
                print("%d = %d + %d + ... + %d" %(cube, i, i+2, j))
            # 没找到，退出内层循环，返回外层for循环
            if sum > cube:
                sum = 0  # 将sum重置为0，以便开始下次试探
                break
            j += 2
        i += 2

