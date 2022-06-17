#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/9 0:09
# @desc: 求矩阵的最值

if __name__ == "__main__":
    row1, row2 = 0, 0   # 行下标
    column1, column2 = 0, 0 # 列下标
    a = [[12, 17, 13, 16], [18, 11, 19, 15], [10, 14, 12, 15]]
    print("打印矩阵：")
    for i in range(3):
        for j in range(4):
            print("%d  " %(a[i][j]), end=" ")
        print()
    max = a[0][0]  # 设置max的初值
    min = a[0][0]  # 设置min的初值
    # 矩阵中每个元素逐一与max进行比较
    for i in range(3):
        for j in range(4):
            if a[i][j] > max:  # 如果某个矩阵元素大于max，则将其与max进行交换
                max= a[i][j]
                row1 = i
                column1 = j
            if a[i][j] < min:  # 如果某个矩阵元素小于min，则将其与min进行交换
                min = a[i][j]
                row2 = i
                column2 = j
    print("矩阵的最大值为：%d，其所在行为第%d行，所在列为第%d列\n" %(max, row1, column1))
    print("矩阵的最小值为：%d，其所在行为第%d行，所在列为第%d列\n" %(min, row2, column2))