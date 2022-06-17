#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/3 0:27
# @desc: 绘制余弦曲线

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 范围0~2π,共100等分
    X = np.linspace(0, 2 * np.pi, 100)  #生成指定大小的一维数组
    Y = np.cos(X)  # 返回数组元组的余弦值

    # 传入数据
    plt.plot(X, Y, linewidth = 4)  # 设置线宽
    plt.plot(X, Y, 'g')  # 设置线条为绿色

    plt.title("余弦曲线图")


    # 保存图片
    plt.savefig("reuslt1.png")
    # 绘制曲线
    plt.show()
