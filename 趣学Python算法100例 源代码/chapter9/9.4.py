#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 20:32
# @desc: 递归解决年龄问题

#递归计算年龄
def age(n):
    if n == 1:
        x = 10
    else:
        x = age(n-1) + 2
    return x

if __name__ == "__main__":
    n = int(input("请输入n值："))   # n表示第几个人
    print("第 %d 个人的年龄为：%d" %(n, age(n)))  # 调用age()函数，计算第n个人的年龄