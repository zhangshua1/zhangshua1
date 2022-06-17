#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/11 0:59
# @desc: 求给定数的位数

if __name__=="__main__":
    print("请输入一个正整数n：", end="")
    n = int(input())
    if n <=0:
        print("输出错误")
        exit()
    count = 0  # count存储数的位数
    while n != 0:
        n = n // 10
        count += 1
    print(" %d 位数" %count)