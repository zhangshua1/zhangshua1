#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/5 1:40 
# @desc: 绘制三维图  首先需要安装 pip install plotly和pandas


import pandas as pd
import plotly
import plotly.graph_objs as go

# 导入数据
data = pd.read_csv("cars.csv")

if __name__ == "__main__":
    # 绘制
    fig1 = go.Scatter3d(x=data['curb-weight'],
                        y=data['horsepower'],
                        z=data['price'],
                        marker=dict(opacity=0.9,
                                    reversescale=True,
                                    colorscale='Blues',
                                    size=5),
                        line=dict (width=0.02),
                        mode='markers')

    # 设置布局
    mylayout = go.Layout(scene=dict(xaxis=dict( title="curb-weight"),
                                    yaxis=dict( title="horsepower"),
                                    zaxis=dict(title="price")),)

    # 保存为html的文件形式
    plotly.offline.plot({"data": [fig1],
                         "layout": mylayout},
                         auto_open=True,
                         filename=("3DPlot.html"))
