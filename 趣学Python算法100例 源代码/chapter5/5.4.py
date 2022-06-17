#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/19 1:30
# @desc: 素数

import math

if __name__ == "__main__":
    flag = 1
    count = 0
    print("请输入一个整数范围(start-end): ")
    start = int(input("start = "))
    end = int(input("end = "))
    while not (start>0 and start<end):  #判断输入范围是否正确
        print("输入的参数有误，请重新输入：" )
        start = int(input("start = "))
        end = int(input("end = "))

    print("%d 和 %d 之间的素数有：" %(start, end))
    # 外层循环，对start-end之间的每个数进行迭代，检查是否为素数
    m = start
    while m <= end:
        k = math.sqrt(m)  # 求m的平方根
        i = 2
        while i <= k:  # 内层循环，判断2-k之间的每个数是否能被m整除
            if m % i == 0: # 若存在一个数能被m整除，则跳出内层循环
                flag = 0
                break
            i += 1
        if flag == 1:  # 如果flag == 1,则当前的m为素数
            print("%-4d" %m, end="")
            count += 1
            if count % 15 == 0:  # 每10个素数换一行
                print()
        flag = 1
        m += 1
    print("\n%d 到 %d之间共有：%d 个素数" %(start, end, count))
