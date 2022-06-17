#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/8/10 14:42
#desc: 绘制奥运五环

import turtle

def huitu_wuhuan():
    turtle.width(8)   #设置宽度

    turtle.color("blue")  #设置画笔颜色
    turtle.circle(50)    #画圆

    turtle.penup()   #抬笔
    turtle.goto(120, 0)  #移动到坐标点
    turtle.pendown()  #下笔

    turtle.color("black")
    turtle.circle(50)

    turtle.penup()
    turtle.goto(240, 0)
    turtle.pendown()

    turtle.color("red")
    turtle.circle(50)

    turtle.penup()
    turtle.goto(60, -50)
    turtle.pendown()

    turtle.color("yellow")
    turtle.circle(50)

    turtle.penup()
    turtle.goto(180, -50)
    turtle.pendown()

    turtle.color("green")
    turtle.circle(50)
    turtle.done()

if __name__=="__main__":
    huitu_wuhuan()