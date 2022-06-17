#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/4 23:34
# @desc: 画直线

import turtle

if __name__ == "__main__":
    # 绘制折线
    turtle.penup()  # 提笔
    turtle.color('green', 'red')
    turtle.goto(100, 100)
    turtle.pendown()  # 落笔

    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.goto(-100, 100)
    turtle.goto(100, 100)
    turtle.goto(5, 215)
    turtle.goto(-108, 90)

    turtle.done()
