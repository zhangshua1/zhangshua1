#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/8/18 18:23
# @desc: 数据加密问题

def encry(n, count):
    i = 0
    while n % 10 > 0 and i < 8:
        s[i] = n % 10
        n = n // 10
        i += 1
        count += 1
    i = 0
    for i in range(count+1):
        s[i] += 5
        s[i] %= 10
    # 交换第一位和最后一位数字
    t = s[0]
    s[0] = s[count-1]
    s[count-1]=t

    #输出加密后的数据
    i = count-1
    while i >= 0:
        print("%d" %s[i], end="")
        i -=1
    print()

if __name__ == "__main__":
    s = [0] * 8  # 数组s用来存放生成的8位数
    n = int(input("请输入将要加密的整数："))
    count = 0
    encry(n, count)