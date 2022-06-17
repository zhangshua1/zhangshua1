#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/11 23:51 
# @desc: 黑洞数

# 求三位数的组合最大值
def three_max(a, b, c):  # a,b,c分别对应百位十位个位
    if a < b:  # 如果a<b，将变量a、b的值互换
        t = a
        a = b
        b = t
    if a < c:
        t = a
        a = c
        c = t
    if b < c:
        t = b
        b = c
        c = t
    return a*100 + b*10 + c

#求三位数的组合最小值
def three_min(a, b, c):  # a,b,c分别对应百位十位个位
    if a < b:  # 如果a<b，将变量a、b的值互换
        t = a
        a = b
        b = t
    if a < c:
        t = a
        a = c
        c = t
    if b < c:
        t = b
        b = c
        c = t
    return c*100 + b*10 + a


# 求黑洞数
def black_number(max, min):
    j = max - min
    k = 0
    while k < min:  # k控制循环次数
        h = j  # h记录上一次最大值与最小值的差
        hun = j // 100  # 百位
        ten = j % 100 // 10  # 十位
        bit = j % 10  # 个位
        max = three_max(hun, ten, bit)  # 最大值
        min = three_min(hun, ten, bit)  # 最小值
        j = max - min
        if j == h:  # 最后两次差相等时，差即为所求黑洞数
            print("%d " % j)
            break  # 跳出循环
        k += 1


if __name__ == "__main__":
    i = int(input("请输入一个三位整数："))
    hun = i // 100   # 百位
    ten = i % 100 // 10   # 十位
    bit = i % 10   # 个位
    max = three_max(hun, ten, bit)  # 最大值
    min = three_min(hun, ten, bit)  # 最小值
    print("max = ", max)
    print("min = ", min)
    black_number(max, min)

