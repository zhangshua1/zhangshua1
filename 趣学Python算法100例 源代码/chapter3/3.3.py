#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/11 22:51
# @desc: 阿姆斯特朗数

if __name__ == "__main__":
    a = [0, 0, 0]  # 列表a用来存储拆分的数的个位，十位，百位
    print("1000以内的阿姆斯特朗数：")
    for i in range(2, 1000):
        t = 0
        k = i
        # 按从低位到高位的顺序拆分数
        while k:
            a[t] = k % 10
            k = k // 10
            t += 1
        sum = a[0]**3 + a[1]**3 + a[2]**3
        if i == sum:
            print("%d \t " %i, end=" ")