#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/20 23:58
# @desc: 素数

import math

if __name__ == "__main__":
    print("请输入一个大于1的整数，判断是不是素数")
    m = int(input("m = "))
    if m <= 1:
        print("输入错误")
        exit()

    # 判断m是否为素数
    k = int(math.sqrt(m))
    for i in range(2, k + 2):
        if m % i == 0:
            break  # 可以整除，肯定不是素数，结束循环
    if i == k + 1:
        print(m, "是素数！")
    else:
        print(m, "不是素数！")
