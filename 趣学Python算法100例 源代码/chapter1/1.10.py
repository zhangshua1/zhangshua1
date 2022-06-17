#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/2 11:34 
# @desc: 数制转换

# 将字符转换成数字
def char_to_num(ch):
    if ch >= '0' and ch <= '9':
        return int(ch)  # 将数字字符转换成数字
    else:
        return ord(ch)  # 将字母字符转换成数字


# 将数字转换为字符
def num_to_char(num):
    if num >= 0 and num <= 9:
        return str(num)  # 将0~9之间的数字转换成字符
    else:
        return chr(num)  # 将大于10的数字转换成字符


# 其他数制转换为十进制
def source_to_decimal(temp, source):
    decimal_num = 0  # 存储展开之后的和

    for i in range(len(temp)):  # 累加
        decimal_num=(decimal_num * source)+char_to_num(temp[i])

    return decimal_num


# 十进制转换为其他数制
def decimal_to_object(decimal_num, object):
    decimal = []
    while decimal_num:
        decimal.append(num_to_char(decimal_num % object))# 求出余数并转换为字符
        decimal_num //= object  # 用十进制数除以基数

    return decimal


# 修改余数数制
def output(decimal):
    f = len(decimal)-1
    while f >= 0:
        print(decimal[f], end='')
        f -= 1
    print()

if __name__ == '__main__':
    MAXCHAR = 101  # 最大允许字符串长度
    flag = 1  # 存储是否退出程序的标志
    while flag:  # 利用输入的flag值控制循环是否结束
        print("转换前的数是：", end='')
        temp = input()
        print("转换前的数制是：", end='')
        source = int(input())
        print("转换后的数制是：", end='')
        object = int(input())
        print("转换后的数是：", end='')
        decimal_num = source_to_decimal(temp, source)
        decimal = decimal_to_object(decimal_num, object)
        output(decimal)
        print("继续请输入1,否则输入0：")
        flag = int(input())
