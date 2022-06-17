#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/6 23:15 
# @desc: numpy库

import  numpy as np

if __name__ == "__main__":
    # 生成一维数组
    a = np.array([1,2,3,4,5,6,7,8,9])
    print("a = ", a)

    print("数组的维度：", a.ndim)

    print("数组的形状：", a.shape)

    print("数组的大小：", a.size)

    print("数组内元素的数据类型：", a.dtype)

    print("数组内元素占计算机内存的大小：", a.itemsize)

    print("数组在内存中的地址：", a.data)

    # 生成二维数组
    b = np.array([[1,3,5],[2,4,6],[7,8,9]])
    print("b = ", b)
    print("数组的维度：", b.ndim)
    print("数组的形状：", b.shape)

    # 生成三维数组，并指定数据类型
    c = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]], dtype=int)
    print("c = ", c)
    print("数组的维度：", c.ndim)
    print("数组的形状：", c.shape)
