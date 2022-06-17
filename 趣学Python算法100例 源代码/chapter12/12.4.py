#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/7 11:14
# @desc: 双色球  红球范围1-33,6个； 蓝球范围1-16，1个

import random

if __name__ == "__main__":
    red = [1] * 6  # 定义red数组，保存随机生成的6个红球号码，号码范围为：1-33
    i = 0
    # 随机生成6个红球号码
    while i < 6:
        tmp = random.randint(1, 33)
        j = 0
        while j < i:
            # 判断已生成的红色球号码是否与当前while循环中产生的随机红色球号码相同
            # 如果相同，则重新生成新的红色球号码，否则在red[i]中保存新生成的红色球号码
            if red[j] == tmp:
                break
            j += 1
        if j == i:
            red[i] = tmp  # 将新生成的红色球号码保存在red数组中
            i += 1

    blue = random.randint(1, 16)  # 随机生成蓝色球号码
    print("本期的开奖号码是：")
    print("红色球：", end=" ")
    for i in range(6):
        print("%d" % red[i], end=" ")
    print("   蓝色球：%d" % blue)



