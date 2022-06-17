#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/12 0:37 
# @desc: 勾股数  a**2+b**2=c**2

import math

if __name__ == "__main__":
    count = 0
    print("100以内的勾股数有：")
    # a,b,c分别表示三角形的三条边
    # 满足勾股数的三个数组成的三角形一定是直角三角形
    print("   a\tb\t c \t\t a \t b \t  c \t\t a \t  b\t  c \t\t a\t b\t  c");
    # 求100以内的勾股数
    for a in range(1,101):
        for b in range(a+1, 101):  # 邻边不能相等，否则就是等边三角形了
            c = int(math.sqrt(a*a + b*b))  # 求c值,并转换为整型
            # 判断c的平方是否等于a*a + b*b ,且两边之和大于第三边
            if c*c == (a*a + b*b) and (a + b > c) and (a + c > b) and (b + c > a) and c <= 100:
                print("%4d %4d %4d\t |" %(a, b, c), end="")
                count += 1
                if count % 4 == 0:
                    print()
