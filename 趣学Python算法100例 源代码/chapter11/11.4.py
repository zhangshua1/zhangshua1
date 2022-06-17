#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/2 23:54
# @desc: 绘制正弦曲线

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    x = np.arange(0, 2 * np.pi, 0.01)   # 从0到2π，以0.01步进
    y = np.sin(x)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
    plt.plot(x, y, linewidth=4)  # 设置线的宽度
    plt.plot(x, y, 'g')  # 设置线条颜色  y:黄色  g:绿色   b:黑色  c:灰色  默认为蓝色
    plt.title("正弦曲线图")   # 图像标题
    plt.show()   # 绘制
