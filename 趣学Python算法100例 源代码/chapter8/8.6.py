#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/26 22:22
# @desc: 邮票组合


if __name__=="__main__":
    a, b, c, d = map(int, input("请输入4种邮票的面值,以空格分割: \n").split())
    stamp = [0]*4   # 存放4种邮票的面值
    stamp[0] = a
    stamp[1] = b
    stamp[2] = c
    stamp[3] = d
    print("你输入的4种邮票面值为：" )
    print(stamp)
    stamp.sort()     # 对邮票面值排序，最大面值为stamp[3],第二大面值为stamp[2],第三大面值为stamp[1]
    sum = stamp[3]*3 + stamp[2]*1 + stamp[1]*1
    print("组合后的最大邮资为：%d" %sum)



