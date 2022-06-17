#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 23:33
# @desc: 杨辉三角

# 杨辉三角递归函数
def c(x, y):
    if y == 1 or y == x:   # y=1或y=x时，函数返回值为1
        return 1
    else:
        z = c(x-1, y-1) + c(x-1, y)   # y为其他值，递推公式
        return z


if __name__ == "__main__":
    n = int(input("请输入杨辉三角的行数："))
    for i in range(1, n+1):   # 输出n行
        for j in range(0, n-i+1):
            print("   ", end=" ")
        for j in range(1, i+1):
            print("%6d  " %(c(i, j)), end=" ")   # 调用递归函数，输出第i行的第j个值
        print()
