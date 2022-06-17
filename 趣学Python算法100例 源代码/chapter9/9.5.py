#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 22:44
# @desc: 递归解决分鱼问题

# 分鱼递归方法
def fish(n, x):
    if (x-1) % 5 == 0:
        if n == 1:
            return 1   # 递归出口
        else:
            return fish(n-1, (x-1)//5 * 4)   # 递归调用
    return 0  # x 不是符合题意的解，返回0

if __name__ == "__main__":
    # 变量定义及初始化
    i = 0
    flag = 0
    while True:
        if flag != 1:
            i += 1
            x = i*5 + 1     # x最小值为6，以后每次增加5
            if(fish(5, x)):  # 将x传入分鱼递归函数进行检验
                flag = 1  # 找到第一个符合题意的x则置标志位为1
                print("五个人合伙捕到的鱼总数为%d" %x);

                exit()  # 结束程序