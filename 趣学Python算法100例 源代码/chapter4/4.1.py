#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/17 1:31
# @desc: 将真分数分解为埃及分数

if __name__ == "__main__":
    print("请输入一个分数：", end=" ")
    a, b = [int(i) for i in input().split()]
    print("输入的分数为：%ld/%ld" %(a, b))
    print("埃及分数：", end=" ")
    while 1:
        if b % a != 0:  # 若分子不能整除分母，则分解出一个分母为b//a+1的埃及数
            c = b // a + 1
        else:
            c = b // a
            a = 1
        if a == 1:
            print("1/%ld\n" %c, end="")
            break
        else:
            print("1/%ld + " %c, end="")
        a = a * c - b   # 求出余数的分子
        b = b * c  # 求出余数的分母
        if a == 3 and b % 2 == 0:  # 若余数分子为3，分母为偶数，输出最后两个埃及数
            print("1/%ld + 1/%ld\n" %(b//2, b))
            break



