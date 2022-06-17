#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/4 22:50
# @desc: 绘制空心菱形

def draw(n):
    # 外层循环控制行数，从控制台输入的参数n即为菱形上半个三角形的行数
    for i in range(1, n + 1):
        for j in range(1, (n + i - 1) + 1):
            if j == n + 1 - i or j == n - 1 + i:
                print("* ", end="")
            else:
                print(" ", end="")
        print()
    # 打印下半个三角形
    # 外层循环控制行数，由于下半个三角形比上面的少一行，所以循环变量i的最大值为n-1
    for i in range(1, n):
        for j in range(1, (2 * n - 1 - i) + 1):
            if j == i + 1 or j == 2 * n - 1 - i:
                print("* ", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    n = int(input("请输入菱形对称轴的行数n: "))
    draw(n)