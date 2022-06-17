#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/4 0:14
# @desc: 三色球问题

if __name__=="__main__":
    # 从12个球中任取8个，红球m个，白球n个，黑球8-m-n个
    # m的取值范围为[0,3]，n的取值范围因此为[0,3]，黑球的个数小于等于6，即8-m-n≤6
    print("\t 红球 \t 白球 \t 黑球")
    print("........................")
    num = 0
    for m in range(0, 4):
        for n in range(0, 4):
            if 8-m-n <= 6:
                num += 1
                print("%2d:  %d \t\t %d \t\t %d" %(num, m, n, 8-m-n))