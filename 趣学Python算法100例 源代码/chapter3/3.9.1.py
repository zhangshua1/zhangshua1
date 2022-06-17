#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/12 1:06 
# @desc: 互质勾股数

if __name__ == "__main__":
    a = int(input("请输入一个a值："))
    if a >= 3 and a % 2 == 1:   # 输入的a为奇数,则a = 2n+1, b=2n**2+2n, c=2n**2+2n+1
        n = (a - 1) // 2
        b = 2 * n**2 + 2*n
        c = 2 * n**2 + 2*n + 1
        print("%d %d %d\n" %(a,b,c))
    else:
        if a >= 3 and a % 2 == 0:  # 输入的a为偶数,则a = 2n, b=n**2-1, c=n**2+1
            n = a // 2
            b = n**2 - 1
            c = n**2 + 1
            print("%d %d %d\n" % (a, b, c))
        else:
            print("error")


