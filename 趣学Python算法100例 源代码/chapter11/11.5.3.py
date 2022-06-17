#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/3 1:08
# @desc: 一元二次方程曲线与圆形

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    x = y = np.arange(-8, 8, 0.1)
    x, y = np.meshgrid(x, y)
    plt.contour(x, y, x ** 2 + y ** 2, [25])  # x**2 + y**2 = 25 的圆形

    # 一元二次方程  y = x^2 - 2x + 1
    x1 = np.linspace(-3, 3, 50)
    print(x1)
    y1 = x1 ** 2
    plt.plot(x1, y1, linewidth=4)  # 设置线宽
    plt.plot(x1, y1, 'g')  # 设置线条为绿色

    plt.title("一元二次方程曲线与圆形")
    plt.axis('scaled')
    plt.show()