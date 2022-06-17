#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/3 1:12
# @desc: 绘制圆形

from math import pi
from numpy import cos, sin
from matplotlib import pyplot as plt

if __name__ == "__main__":

    angles_circle = [i * pi / 180 for i in range(0, 360)]  # i先转换成double
    # angles_circle = [i/np.pi for i in np.arange(0,360)]             # <=>
    # angles_circle = [i/180*pi for i in np.arange(0,360)]    X
    x = cos(angles_circle)
    y = sin(angles_circle)
    plt.plot(x, y, 'r')

    plt.axis('equal')
    plt.axis('scaled')
    plt.show()