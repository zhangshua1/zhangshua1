#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/6 0:53 
# @desc: 马克思手稿中的数学题

if __name__=="__main__":
    # 变量x、y和z分别代表男人、女人和小孩
    print("    Men  Women  Children ")
    number = 0   # 可能的值的组数
    x = 0   # 男人的取值范围为[0-10]
    while x <= 10:
        y = 20 - 2 * x   # 当x一定时，可以确定y
        z = 30 - x - y   # 当x,y一定时，可以确定z
        if 3 * x + 2 * y + z == 50:
            number += 1
            print("%2d:%4d%5d%6d"  %(number, x, y, z))
        x += 1