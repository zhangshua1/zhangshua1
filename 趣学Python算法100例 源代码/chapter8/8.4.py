#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/26 21:52
# @desc: 狼追兔子

if __name__=="__main__":
    n = 0
    x = 0
    a = [1]*11   # 定义一个长度为11的数组，初始值均为1
    for i in range(0, 1000):   # 穷举搜索
        n += (i+1)
        x = n % 10
        a[x] = 0    # 没有找到，设置为0
    for i in range(0, 10):   # 输出结果
        if a[i]:
            print("可能在第%d个洞中" %i)