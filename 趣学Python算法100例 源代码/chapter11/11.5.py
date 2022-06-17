#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/3 0:41
# @desc: 绘制圆形

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 圆半径
    r = 2.0
    # 圆心坐标
    a , b = (0. , 0.)
    # 方法一：参数方程
    Circle = np.arange(0, 2*np.pi, 0.01)
    x = a + r * np.cos(Circle)
    y = b + r * np.sin(Circle)
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)
    axes.axis('equal')
    plt.title("圆形")
    plt.show()