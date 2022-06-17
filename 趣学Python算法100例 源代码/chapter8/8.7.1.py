#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/9 0:52 
# @desc: 魔方矩阵

if __name__ == "__main__":
    N = 5
    a = [[0] * 5 for i in range(5)]  # 定义一个5*5的二维数组
    i = 0   # 自然数1的行标
    j = N // 2  # 自然数1的列标
    t = N - 1
    k = 1
    while k <= (N * N):  # 变量k控制循环和自然数
        a[i][j] = k
        x = i # 变量x保存新的行
        y = j # 变量y保存新的列
        if i == 0:
            i = t  # 当前数在第0行，则下一个数在最后一行
        else:
            i = i - 1  # 产生行，非第0行则取下一列
        if j != t:
            j = j + 1  # 产生列，非最后列则取下一列
        else:
            j = 0   # 当前数在最后一列，则下一个数在第一列
        if a[i][j] != 0:
            i = x + 1
            j = y
        k += 1
    # 打印生成的魔方阵
    print("生成的5-魔方阵为：", end="")
    for i in range(N):
        print()
        for j in range(N):
            print("%3d " %a[i][j], end=" ")
    print()