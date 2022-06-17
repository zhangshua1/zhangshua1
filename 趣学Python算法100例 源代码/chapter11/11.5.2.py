#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/3 1:06
# @desc: 绘制圆形和椭圆

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ell1 = Ellipse(xy=(0.0, 0.0), width=4, height=8, angle=30.0, facecolor='yellow', alpha=0.3)
    cir1 = Circle(xy=(0.0, 0.0), radius=2, alpha=0.5)
    ax.add_patch(ell1)
    ax.add_patch(cir1)

    x, y = 0, 0
    ax.plot(x, y, 'ro')

    plt.axis('scaled')
    # ax.set_xlim(-4, 4)
    # ax.set_ylim(-4, 4)
    plt.axis('equal')  # changes limits of x or y axis so that equal increments of x and y have the same length

    plt.show()