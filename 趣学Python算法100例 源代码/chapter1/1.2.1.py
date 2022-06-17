#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/1 2:09
# @desc: 兔子产子问题

if __name__=="__main__":
    fib1 = 1
    fib2 = 1
    i = 1
    while i <= 15:  #每次求两个，因此循环变量循环到15
        print("%8d    %8d" %(fib1, fib2), end="      ")
        if i % 2 == 0:
            print()
        fib1 = fib1 + fib2  # 最新一个月的兔子数
        fib2 = fib1 + fib2  # 第4个月的兔子数
        i += 1
