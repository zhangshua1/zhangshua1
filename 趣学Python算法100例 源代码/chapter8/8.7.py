#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/9 0:29 
# @desc: 魔方矩阵

def array(n):
    if n % 2 == 0:   # n是偶数，则加1使其变为奇数
        n = n + 1
    max = n * n
    mtrx = [1] * max
    mtrx[n // 2] = 1  # 将1存入数组
    i = 0   # 自然数1所在行
    j = n // 2  # 自然数1所在列
    # 从2开始确定每个数的存放位置
    for num in range(2, max + 1):
        i = i - 1
        j = j + 1
        if (num - 1) % n == 0:  # 当前数是n的倍数
            i = i + 2
            j = j - 1
        if i < 0:  # 当前数在第0行
            i = n - 1
        if j > n - 1:  # 当前数在最后一列，即n-1列
            j = 0
        no = i * n + j  # 找到当前数在数组中存放的位置
        mtrx[no] = num
    # 打印生成的魔方矩阵
    print("生成的%d-魔方阵为：" %n, end="")
    no = 0
    for i in range(0, n):
        print()
        for j in range(0, n):
            print("%3d" %mtrx[no], end=" ")
            no += 1
    print()

if __name__ == "__main__":
    n = int(input("请输入n值："))
    array(n)  # 调用array函数