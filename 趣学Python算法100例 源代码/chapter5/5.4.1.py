#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/20 23:54
# @desc: 素数

if __name__ == "__main__":
    print("请输入一个大于1的整数，判断是不是素数")
    m = int(input("m = "))
    if m <= 1:
        print("输入错误")
        exit()
    if m == 2:
        print("2 是素数")
    else:
        # 判断m是否为素数
        i = 2
        while i <= m:
            if m % i == 0:
                print("%d 不是素数！" %m)
                break
            i = i + 1
        else:
            print("%d 是素数！" %m)
