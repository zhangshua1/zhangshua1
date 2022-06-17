#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/29 22:23
# @desc: 角谷猜想
# 任给一个自然数，若为偶数则除以2，若为奇数则乘以3再加1，
# 这样得到一个新的自然数之后再按照前面的法则继续演算，若干次以后得到的结果必然为1

if __name__ == "__main__":
    count = 0
    n = int(input("请输入一个自然数："))
    while n != 1:   # 当n=1时终止循环
        if n % 2 == 1:   # 若n为奇数，则乘以3加1
            n = n * 3 + 1
            count += 1
            print("[%d]: %d * 3 + 1 = %d " %(count, (n-1)//3, n))  # 输出执行步骤
        else:
            n //= 2   # 若n为偶数，则直接除以2
            count += 1
            print("[%d]: %d / 2 = %d " %(count, 2 * n, n))  # 输出执行步骤