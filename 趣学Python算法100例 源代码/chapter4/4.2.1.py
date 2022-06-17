#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/18 1:27
# @desc: 列出真分数序列


if __name__ == "__main__":
    print("分母为40，分子小于40的最简分数有：")
    n = 0  # 计数器，记录最简分数的个数
    for i in range(1, 40):  # 穷举40以内的全部分子
        num1 = 40  # 分母
        num2 = i  # 分子
        j =2
        while j <= num2:
            # 判断2～num2之间分子、分母是否有公约数
            # 如果有j满足条件，则结束循环，说明此时的分数不是最简分数
            if (num1 % j == 0) and (num2 % j == 0):
                break
            j += 1
        # 如果j > num2说明2~num2之间没有分子，分母的公约数，分数为最简分数
        if j > num2:
            print("%2d/40  " %i, end=" ")
            n += 1
            if n % 8 == 0:   # 每行输出8个数
                print()

