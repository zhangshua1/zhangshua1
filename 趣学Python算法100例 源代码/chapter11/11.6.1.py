#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/4 23:07
# @desc: 绘制实心菱形

def draw(n):
    a = "*"*(2*(6-n)+1)
    print(a.center(11, ' '))
    if n != 1:
        draw(n-1)   # 递归调用
        print(a.center(11, ' '))

if __name__ == "__main__":
    n = int(input("请输入菱形对称轴的行数n："))
    draw(n)