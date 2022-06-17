#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/9 0:03
# @desc: 矩阵转置

if __name__ == "__main__":
    n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("原始矩阵：")
    for i in range(3):
        for j in range(3):
            print("%d  " %(n[i][j]), end=" ")  # 输出原始矩阵
        print()

    for i in range(3):
        for j in range(3):
            if j > i:   #将主对角线右上方的数组元素与主对角线左下方的数组元素进行单方向交换
                temp = n[i][j]
                n[i][j] = n[j][i]
                n[j][i] = temp

    print("转置矩阵：")
    for i in range(3):
        for j in range(3):
            print("%d  " %(n[i][j]), end=" ")
        print()