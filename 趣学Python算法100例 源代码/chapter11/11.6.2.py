#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/4 23:24
# @desc: 使用 turtle 库绘制菱形

import turtle

if __name__ == "__main__":
    turtle.right(-45)  # 起始顶点绝对角度设为正30度
    for i in range(4):   # 画四边，转向4次
        turtle.fd(200)
        angle = 60 * (1 + i%2)  # 其他3顶点右转角度分别为60,120,60度
        turtle.right(angle)
    turtle.done()
