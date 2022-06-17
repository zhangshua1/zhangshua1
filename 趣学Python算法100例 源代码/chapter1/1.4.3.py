#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/13 10:33
# @desc: 百钱白鸡问题

if __name__=="__main__":
    #cock表示公鸡，hen表示母鸡，chicken表示小鸡，总共100只
    # 外层循环控制公鸡数量取值范围0~20
    cock = 0
    while cock <= 20:
        # 内层循环控制母鸡数量取值范围0~33
        hen = 0
        while hen <= 33:
            #内层循环控制小鸡数量取值范围0~100
            chicken = 0
            while chicken <= 100:
                if (5 * cock + 3 * hen + chicken / 3.0 ==100) and (cock + hen + chicken ==100):
                    print("cock=%2d,hen=%2d,chicken=%2d\n" %(cock,hen,chicken))
                chicken += 1
            hen += 1
        cock += 1