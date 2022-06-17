#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/5/29 0:19
# @desc: 百钱白鸡问题

if __name__=="__main__":
    # 外层循环控制公鸡数量取整范围0-20
    cock = 0
    while cock <= 20:
        # 内层循环控制母鸡数量取值范围为0-30
        hen = 0
        while hen <= 33:
            # 小鸡的数量
            chicken = 100 - cock - hen
            if 5 * cock + 3 * hen + chicken / 3.0 == 100:
                print("cock=%2d,hen=%2d,chicken=%2d\n" %(cock, hen, chicken))
            hen+=1
        cock+=1
