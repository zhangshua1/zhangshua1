#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/10 15:16 
# @desc: 绘制折线图

import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    np.random.seed(19680801)  # 随机数种子
    fig = plt.figure()  # 创建图形
    ax = fig.add_subplot(111)
    ax.plot(100 * np.random.rand(20))
    formatter = ticker.FormatStrFormatter('$%1.2f')  # 设置标记的格式
    ax.yaxis.set_major_formatter(formatter)  # 设置y轴的主要标记
    # 设置y轴刻度的属性
    for tick in ax.yaxis.get_major_ticks():
        tick.label1On = False
        tick.label2On = True
        tick.label2.set_color('green')
    plt.show()