#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/1 16:29
# @desc: 绘图，计算(x1,y1)到(x4,y4)的距离

import turtle
import math

if __name__=="__main__":
    # 定义多个点的坐标
    x1, y1 = 100, 100
    x2, y2 = 100, -100
    x3, y3 = -100, -100
    x4, y4 = -100, 100
    x5, y5 = 100, 100

    # 绘制折线
    turtle.penup()  # 提笔
    turtle.goto(x1, y1)
    turtle.pendown()  # 落笔

    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    turtle.goto(x5, y5)

    # 计算起始点和终点的距离
    distance = math.sqrt((x1-x4)**2 + (y1-y4)**2)
    turtle.write(distance)
    turtle.done()


