#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/29 22:42
# @desc: π的近似值 ——蒙特卡罗法求解

from random import random
import math

if __name__ == "__main__":
    DARTS = 300000000     # 落入正方形的总的点数,此数越大，越逼近π的近似值
    hits = 0.0      # 落入四分之一圆的点数
    for i in range(1, DARTS+1):
        x, y = random(), random()    # 随机生成[0, 1)之间的数
        dist = math.sqrt(x**2+y**2)   # 蒙特卡罗法求解
        if dist <= 1.0:
            hits = hits+1
    pi = 4*(hits/DARTS)   # 计算π的近似值
    print("pi的值{}.".format(pi))

