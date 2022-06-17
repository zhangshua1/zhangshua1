#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/5 0:10
# @desc: 画圆和圆弧

import turtle

if __name__ == "__main__":
    # 画脸
    turtle.width(2)  # 设置宽度
    turtle.color("black")  # 设置画笔颜色
    turtle.circle(120)  # 画圆

    # 画眼睛
    turtle.penup()  # 抬笔
    turtle.goto(-60, 130)  # 移动到坐标点
    turtle.pendown()  # 下笔
    turtle.color("black")
    turtle.circle(20)

    turtle.penup()  # 抬笔
    turtle.goto(60, 130)  # 移动到坐标点
    turtle.pendown()  # 下笔
    turtle.color("black")
    turtle.circle(20)

    # 画鼻子
    turtle.penup()  # 抬笔
    turtle.goto(0, 120)  # 移动到坐标点
    turtle.pendown()  # 下笔
    turtle.goto(-50, 70)
    turtle.goto(50, 70)
    turtle.goto(0, 120)

    # 画嘴巴
    turtle.penup()  # 抬笔
    turtle.goto(-60, 45)  # 移动到坐标点
    turtle.pendown()  # 下笔
    #turtle.circle(90, extent= 90)
    turtle.setheading(90) #设置朝向
    len = 1  # 设置初始走的速度为1
    for j in range(60):
        if j > 30:  # 当j<30，也就是画前一半的弧线
            len += 0.2  # 让速度越走越快
        else:  # 画后一半弧线
            len -= 0.2  # 让速度越走越慢
        turtle.forward(len) #前进
        turtle.left(3) # 左转
    turtle.goto(-60, 45)

    turtle.done()  # 关闭
