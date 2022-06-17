#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author:liuhefei
#desc: 谁是窃贼


if __name__ == "__main__":
    #甲乙丙丁分别用A，B，C，D代表。A，B，C，D的值要么为 1，要么为 0.
    # 为 1 表示是窃贼， 为 0 表示不是
    # 满足四个条件： B+D=1, B+C=1, A+B=1, A+B+C+D=1
    A, B, C, D = 1, 0, 0, 0
    for i in range(1, 4+1):  #i=1,2,3,4
        if B+D == 1 and B+C == 1 and A+B == 1:
            break
        else:
            if i == 1:
                A=0
                B=1
            if i == 2:
                B=0
                C=1
            if i == 3:
                C=0
                D=1
    print("判断结果：")
    if i == 1:
        print("甲是窃贼\n")
    if i == 2:
        print("乙是窃贼\n")
    if i == 3:
        print("丙是窃贼\n")
    if i == 4:
        print("丁是窃贼\n")

