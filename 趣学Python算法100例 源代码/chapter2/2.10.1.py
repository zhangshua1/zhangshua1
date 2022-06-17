#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/20 10:12 
# @desc: 马克思手稿中的数学题

if __name__=="__main__":
    # 变量x、y和z分别代表男人、女人和小孩
    print("    Men  Women  Children ")
    number = 0   # 可能的值的组数
    # 将变量x的可能取值依次代入方程组
    for x in range(0, 10+1):
        y = 20 - 2*x   # 方程3，当x一定时，可确定y值
        z = 30 -x - y  # 方程1，当x, y一定时，可确定z值
        # 代入方程2检验，当前获得的x,y,z是否为不定方程组的一组解
        if 3*x + 2*y + z == 50:
            number += 1
            print("%2d:%4d%5d%6d" % (number, x, y, z))