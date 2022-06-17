#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/9 0:39
# @desc: 亲密数

if __name__=="__main__":
    print("3000以内的全部亲密数为：")
    for a in range(1, 3000):   # 穷举30000以内的全部整数
        b = 0
        i = 1
        while i <= (a//2):   # 计算数 a 的各因子，各因子之和存放到b中
            if a % i == 0:
                b += i
            i += 1

        n = 0  # 计算b的各因子，各因子之和存于 n
        j = 1
        while j <= (b//2):
            if b % j == 0:
                n += j
            j += 1
        if n == a and a < b:
            print("%4d -- %4d \t" %(a, b))


