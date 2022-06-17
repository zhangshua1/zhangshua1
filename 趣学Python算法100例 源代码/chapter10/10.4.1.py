#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/29 22:18
# @desc: 四方定理

import math

if __name__ == "__main__":
    number = int(input("请输入一个自然数："))
    n = int(math.sqrt(number))
    # 穷举各种情况
    for x1 in range(0, n):
        for x2 in range(0, x1+1):
            for x3 in range(0, x2+1):
                for x4 in range(0, x3+1):
                    # 判断是否满足定理要求
                    if number == x1*x1 + x2*x2 + x3*x3 + x4*x4:
                        # 若满足定理要求，则输出其一组解，并退出循环
                        print("%d=%d*%d+%d*%d+%d*%d+%d*%d" %(number, x1, x1, x2, x2, x3, x3, x4, x4))
                        exit(0)  # 退出循环  要想输出多组解，可以注释此行