#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/7 1:15 
# @desc: 掷骰子

import random
import time

if __name__ == "__main__":
    c1 , c2 = 0, 0  # c1,c2分别记录两个人的获胜盘数
    print("两人开始掷骰子100次：")
    for i in range(1, 101):   # 100盘
        d1 , d2 = 0, 0  # d1,d2分别记录两个人投掷点数的累加和
        for j in range(1, 7):    # 两个人轮流掷骰子
            d1 = d1 + random.randint(1, 6)   # 第一个人所掷骰子点数总和
            d2 = d2 + random.randint(1, 6)   # 第二个人所掷骰子点数总和
        if d1 > d2:
            c1 += 1   # 累加获胜盘数
        else:
            if d1 < d2:
                c2 += 1

    print("等待结果......")
    time.sleep(5)
    print("100次之后，获胜者是：")
    if c1 > c2:   # 输出最终获胜者信息
        print("第一个人获胜！")
    else:
        if c1 < c2:
            print("第二个人获胜！")
        else:
            print("两人平局！")


