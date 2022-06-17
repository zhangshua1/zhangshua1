#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/6 20:20
# @desc: 抢30

import random

# 定义输入函数
def input_num(t):
    a = int(input("Please count:"))
    while a > 2 or a < 1 or a + t > 30:

        if a > 2 or a < 1 or a + t > 30:
            print("Error input, again!")
        else:
            print("You count: %d" % (t + a))
        a = int(input("Please count:"))
    print("You count: %d" % (t + a))
    return t + a  # 返回当前已经取走的数的累加和


# 计算谁会胜利
def copu(s):
    c = 0
    print("Computer count: ", end="")
    if (s + 1) % 3 == 0:  # 若剩余的数的模为1，则取1
        s = s + 1
        print(s)
    else:
        if (s + 2) % 3 == 0:
            s = s + 2  # 若剩余的数的模为2，则取2
            print(s)
        else:
            c = random.randint(1, 2)  # 否则随机取1或2
            s = s + c
            print(s)
    return s


if __name__ == "__main__":
    tol = 0
    print("***********catch thirty **************")
    print("Game Begin")
    # 取随机数决定机器和人谁先走第一步。若为1，则表示人先走第一步
    if (random.randint(1, 2) == 1):
        tol = input_num(tol)
    while tol != 30:  # 游戏结束条件
        tol = copu(tol)
        if tol == 30:  # 计算机取第一个数，若为30则机器胜利
            print("Computer: I lose !")
        else:
            tol = input_num(tol)
            if tol == 30:  # 人取一个数，若为30则人胜利
                print("People: I lose !")
    print("************Game Over********************")
