#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/29 21:17
# @desc: 四方定理
# 所有的自然数至多只要用四个数的平方和就可以表示出来

if __name__ == "__main__":
    number = int(input("请输入一个自然数："))
    # 穷举各种情况
    for x1 in range(0, number//2):
        for x2 in range(0, x1+1):
            for x3 in range(0, x2+1):
                for x4 in range(0, x3+1):
                    # 判断是否满足定理要求
                    if number == x1*x1 + x2*x2 + x3*x3 + x4*x4:
                        # 若满足定理要求，则输出其一组解，并退出循环
                        print("%d=%d*%d+%d*%d+%d*%d+%d*%d" %(number, x1, x1, x2, x2, x3, x3, x4, x4))
                        exit(0)  # 退出循环

