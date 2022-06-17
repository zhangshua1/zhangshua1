#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/1 1:52
# @desc: 兔子产子问题

if __name__=="__main__":
    fib1 = 1
    fib2 = 1
    i = 3
    # 输出第一个月和第二个月的兔子数
    print("%6d       %6d" %(fib1, fib2), end="       ")
    while i <= 30:
        fib = fib1 + fib2  # 迭代求出当前月份的兔子数
        print("%6d" %fib, end="       ")   # 输出当前月份兔子数
        if i % 4 == 0:
            print()   # 每行输出4个
        fib2 = fib1  # 为下一次迭代做准备，求出新的flb2
        fib1 = fib   # 求出新的fib1
        i += 1
