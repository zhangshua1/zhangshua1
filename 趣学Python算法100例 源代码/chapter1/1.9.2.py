#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/1 23:57 
# @desc: 二分查找算法, 前提是列表要有序

# 选择排序
def selectionSort(a):
    # 求出列表的长度
    n = len(a)

    for i in range(0, n-1):
        for j in range(i+1, n):
            #交换
            if a[j] < a[i]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    return a


# 二分查找算法，a为输入的列表， m为要查找的元素
def binarySearch(a, m):
    # 获取列表的长度
    n = len(a)
    low = 0  # 列表的起始位置（下界）
    high = n-1  #列表的末尾位置（上界）
    k = -1
    while low <= high:
        # 确定列表中间值的位置
        mid = (low + high) // 2   # //表示整数除法
        if m < a[mid]:
            high = mid -1
        else:
            if m > a[mid]:
                low = mid + 1
            else:
                k = mid
                break

    if k >= 0:
        print("m = %d, index = %d" %(m, k))
    else:
        print("Not be found!")


if __name__=="__main__":
    while True:
        print("请输入一个列表，空格分割，末尾不能有空格：")   # 注意输入的列表的末尾不能有空格，否则将会报错
        x = input()
        a = x.split(" ")  # 以空格方式分割每个元素
        for i in range(0, len(a)):  # 输入多个值
            a[i] = int(a[i])

        # print("你输入的列表元素为：\n", a)
        m = int(input("请输入你要查找的元素: \n"))

        # 以防输入的列表不是有序的，我们先调用排序方法，排好序之后再进行二分查找
        list = selectionSort(a)
        print("排序后的列表：")
        for i in list:
            print(i, end=" ")
        print("\n查找结果：")
        binarySearch(list, m)