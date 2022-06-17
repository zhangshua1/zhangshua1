#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/7 12:27
# @desc: 数据加密问题

def encry(n):
    # 获取各个位上的数
    s[0] = n % 10  # 将个位存入s[0]
    s[1] = n % 100 // 10  # 将十位存入s[1]
    s[2] = n % 1000 // 100  # 将百位存入s[2]
    s[3] = n // 1000  # 将千位存入s[3]

    for i in range(0, 4):
        s[i] += 5  # 各个位数加5
        s[i] %= 10  # 除以10取余

    # 数字交换， 1,4位交换，2,3位交换
    for i in range(0, (3 // 2) + 1):
        # 数据交换
        t = s[i]
        s[i] = s[3 - i]
        s[3 - i] = t

    # 输出加密后的数据
    i = 3
    while i >= 0:
        print("%d" % s[i], end="")
        i -= 1

if __name__ == "__main__":
    s = [0]*4   # 数组s用来存放生成的4位数
    n = int(input("请输入将要传递的四位整数："))
    encry(n)

