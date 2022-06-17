#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/11 1:04
# @desc: 自守数

if __name__=="__main__":
    print("100000以内的自守数：")
    for number in range(0, 100000):
        mul = number
        k = 1
        while (mul // 10) > 0:   # 由number的位数确定截取数字进行乘法时的系数k
            mul //= 10
            k *= 10

        a = k * 10  # a为截取部分积时的系数
        mul = 0 # 积的最后n位
        b = 10  # b为截取乘数相应位时的系数
        while k > 0:
            # (部分积+截取被乘数的后N位*截取乘数的第M位)，%a再截取部分积
            mul = (mul + (number % (k * 10))*(number % b - number % (b //  10)))%a
            k //= 10  # k为截取被乘数时的系数
            b *= 10
        if number == mul:  # 判定若为自守数则输出
            print("%ld " %number, end="\t")
    # print()
