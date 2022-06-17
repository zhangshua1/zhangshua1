#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/3 0:57
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
    # 方法二：标准方程
    x = np.arange(a-r, a+r, 0.01)
    y = b + np.sqrt(r**2 - (x - a)**2)
    flg = plt.figure()
    axes = flg.add_subplot(111)
    axes.plot(x, y)  # 上半圆
    axes.plot(x, -y)  # 下半圆
    plt.axis('equal')
    plt.title("圆形")
    plt.show()