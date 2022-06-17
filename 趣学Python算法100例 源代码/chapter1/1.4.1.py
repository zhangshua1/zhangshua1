#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/5/29 0:14
# @desc: 百钱白鸡问题

if __name__=="__main__":
    # cock表示公鸡，hen表示母鸡，chicken表示小鸡，总共100只
    # 外层循环控制公鸡数量取值范围0~20
    for cock in range(0, 21):
        # 内层循环控制母鸡数量取值范围0~33
        for hen in range(0, 34):
            chicken =100 - cock -hen
            if 5 * cock + 3 * hen + chicken / 3.0 == 100:
                print("cock=%2d,hen=%2d,chicken=%2d\n" %(cock, hen, chicken))
