#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 23:31
# @desc: 猴子吃桃

if __name__ == "__main__":
    day = 9
    x2 = 1
    while day > 0:
        x1 = (x2 + 1) * 2  # 第1天的桃子数是第2天桃子数加1后的2倍
        x2 = x1
        day -= 1
    print("猴子第一天总共摘了 %d 个桃子" %x1)
