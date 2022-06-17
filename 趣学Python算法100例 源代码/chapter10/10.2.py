#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/30 0:07
# @desc: 奇数平方的有趣性质
# 任意奇数的平方有如下的有趣性质：任意奇数的平方与1的差是8的倍数。

if __name__ == "__main__":
    # 对1000到2000范围内的所有奇数进行验证
    n = 1001
    while n <= 1999:
        print("%d: " %(n), end=" ")   # 输出当前的奇数
        print("(%d*%d-1)/8" %(n, n), end=" ")
        print("= %d" %((n*n-1)//8), end=" ")   # 输出(n*n-1)/8的值
        print("+ %d\n" %((n*n-1)%8), end=" ")  # 输出（n*n-1）/8的余数
        n += 2

