#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/13 18:49
# @desc: 折半查找

if __name__ == "__main__":
    a = [-3, 4, 7, 9, 13, 45, 67, 89, 100, 180]
    k = -1  # 记录下标
    print("a数组中的数据如下：")
    for i in a:
        print(i, end=" ")  # 输出数组中原数据序列
    print()
    m = int(input("Enter m = : "))  # 变量m为要查找的整数
    i = 0
    while i < len(a):
        if m == a[i]:
            k = i
            break   # 一旦找到所要查找的元素便跳出循环
        i += 1
    if k >= 0:
        print("m = %d, index = %d" %(m, k))
    else:
        print("Not be found!")

