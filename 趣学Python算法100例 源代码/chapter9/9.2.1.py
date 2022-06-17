#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 23:47
# @desc: 杨辉三角形

if __name__ == "__main__":
    n = 0
    a = [([0] * 14) for i in range(14)]  # 定义一个行为14，列为14的二维数组
    while n <= 0 or n >= 13:   # 控制打印的行数，行数过大会造成显示不规范
        n = int(input("请输入杨辉三角的行数："))
    print("打印 %d 行杨辉三角如下：" %n)
    # 计算杨辉三角中的数值并存入二维数组a中
    for row in range(1, n+1):
        a[row][1] = a[row][row] = 1  # 令每行两边的数为1，循环从1开始，每行第一个数存放在a[row][1]中
    for row in range(3, n+1):
        for column in range(2, (row-1)+1):
            # 计算其他位置的值并存入二维数组
            a[row][column] = a[row-1][column-1] + a[row-1][column]
    # 打印杨辉三角
    for row in range(1, n+1):
        for k in range(1, (n-row)+1):
            print("   ", end="")  # 在每行输出数之前先打印空格占位，使输出更美观
        for column in range(1, row+1):  # column<=row表示不输出数组中其他的数，只输出所需的数
            print("%6d" %(a[row][column]), end=" ")
        print()  # 当一行输出完以后换行继续下一行的输出