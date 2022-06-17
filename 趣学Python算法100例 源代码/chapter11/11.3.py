#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/5 1:10
# @desc: 画彩色图形

import turtle

if __name__ == "__main__":
    t = turtle.Pen()   # 启用画笔
    turtle.bgcolor("white")  # 设置画板背景颜色
    sides=6  # 图形边数
    colors=["red","yellow","green","blue","orange","purple"]  # 颜色列表
    for x in range(360):
        t.pencolor(colors[x%sides])  # 设置画笔颜色
        t.forward(x*3/sides+x)  # 前进
        t.left(360/sides+1)   # 左转
        t.width(x*sides/200)  # 画笔宽度