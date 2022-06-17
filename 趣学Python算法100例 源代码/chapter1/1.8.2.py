#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/1 22:53
# @desc: 冒泡排序

def bubbleSort(a):
    # 首先获取列表list的总长度，为之后循环比较做准备
    n = len(a)
    # 进行 n-1 次比较,控制比较的轮数
    i = 1
    while i <= n-1:
        # 控制每轮比较的次数
        j = 0
        while j < n-i:
            # 交换
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
            j += 1
        i += 1
    # 打印每一轮交换后的列表
    for a1 in a:
        print(a1, end=" ")


if __name__=="__main__":
    print("请为列表元素赋初值，列表末尾不能有空格：")
    x = input()
    a = x.split(" ")  # 以空格方式分割每个元素
    for i in range(0, len(a)):  # 输入多个值
        a[i] = int(a[i])
    print("你输入的列表元素为：\n", a)
    print("经过交换后的数组元素为：")
    bubbleSort(a)
