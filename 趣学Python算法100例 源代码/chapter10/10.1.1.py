#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/29 23:31
# @desc:  尼科彻斯定理
# 任何一个整数的立方都可以表示成一串连续的奇数的和。

if __name__ == "__main__":
    n = int(input("请输入大于1的n值："))
    if n <= 1:
        print("输入的n值有误")
        exit()
    cube = n ** 3   # cube存放n的立方
    print("%d * %d * %d = %d = " %(n, n, n, cube), end="")
    s = 0 # s表示数列的前n项和
    i = 0 # i表示数列的第i项
    while i < n:   # 输出数列，首项为n*n-n+1,公差为2
        s += n * n - n + 1 + i * 2  # 求数列的前n项和
        y = "+ %d" if i else "%d"
        print(y %(n * n - n + 1 + i * 2), end=" ")  # 打印结果
        i += 1
    if s == cube:
        print(" 定理成立")
    else:
        print(" 定理不成立")

