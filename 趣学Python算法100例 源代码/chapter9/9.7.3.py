#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/28 1:18 
# @desc: 递归求最大公约数

# 递归函数 求最大公约数
def gcd(m , n):
    if n == 0:
        g = m
    else:
        g = gcd(n, m % n)  # 递归调用
    return g

if __name__ == "__main__":
    print("请输入两个正整数：")
    m = int(input("m = "))
    n = int(input("n = "))
    g = gcd(m, n)  # 调用递归函数
    print("%d和%d的最大公约数是：%d" %(m, n, g));