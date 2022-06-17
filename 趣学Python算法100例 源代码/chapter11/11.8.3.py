#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/10 23:32 
# @desc: 绘制散点图

import matplotlib.pyplot as plt
import numpy as np

# 定义生成y值的函数
def cData(n):
    a1 = np.cos(2 * np.pi * n)
    b1 = np.exp(-n)
    return a1 * b1

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    d1 = np.arange(0.0, 6.0, 0.3)  # 生成一维数组序列
    point = plt.plot(d1, cData(d1), 'ro')  # 绘制
    plt.setp(point, 'markersize', 20)  # 设置数据点的大小
    plt.setp(point, 'markerfacecolor', 'g') # 设置数据点的颜色
    plt.title('散点图')
    plt.show()
