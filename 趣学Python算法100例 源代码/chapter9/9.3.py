#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/28 0:00
# @desc: 卡布列克常数

# 将输入的4位数拆分存入数组
def createArray(n):
    array = [0] * 4  # 定义数组array[4]，用来存放分解后四位整数num中每位上的数字
    # 分解整数n
    a = n // 1000  # 千位
    b = (n % 1000) // 100  # 百位
    c = ((n % 1000) % 100) // 10  # 十位
    d = ((n % 1000) % 100) % 10  # 个位
    array[0] = a
    array[1] = b
    array[2] = c
    array[3] = d
    # print(array)
    return array

# 求数组的最大值
def array_max(array):
    array.sort()
    maxNum = array[3]*1000 + array[2]*100 + array[1]*10 + array[0]
    # print("maxNum = %d" %maxNum)
    return maxNum

# 求数组的最小值
def array_min(array):
    array.sort()
    minNum = array[0]*1000 + array[1]*100 + array[2]*10 + array[3]
    # print("minNum = %d" %minNum)
    return minNum

# 递归求卡布列克常数
def kblk(n, count):
    if n != 6174 and n != 0:  # 若不等于6174且不等于0则进行卡布列克运算
        array = createArray(n)  # 将四位整数分解，各位数字存入array数组中
        max = array_max(array)  # 求各位数字组成的最大值
        min = array_min(array)  # 求各位数字组成的最小值
        num = max - min  # 求最大值和最小值的差
        count += 1
        print("[%d]: %d-%d=%d\n" % (count, max, min, num));  # 输出该步计算过程
        kblk(num, count);  # 递归调用，继续进行卡布列克运算


if __name__ == "__main__":
    n = 1000
    count = 0
    while n <= 1000 or n > 9999:
        n = int(input("请输入一个4位整数："))
    kblk(n, count)
