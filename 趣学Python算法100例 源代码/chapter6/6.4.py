#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author:liuhefei
#desc: 谁家孩子跑的最慢

if __name__ == "__main__":
    scope = [([0] * 4) for i in range(4)]   #定义列表,用来存储各个孩子的分数
    # score[1]，score[2]，score[3]分别存放张家，王家，李家三个孩子的分数
    #获得第一名的是李家的孩子，获得第二名的是王家的孩子

    #初始化三家孩子的最高分数值
    scope[1][1] = 7    #score[1]存放张家三个孩子的分数
    scope[2][1] = 8    #score[2]存放王家三个孩子的分数
    scope[3][1] = 9    #score[3]存放李家三个孩子的分数

    #通过循环得到9个孩子的分数
    for zhang in range(4, 6):
        for wang in range(4, 7):
            for li in range(4, 7):
                #9个孩子名次不存在并列的情况
                if zhang != wang and li != zhang and li != wang \
                        and 15-zhang-scope[1][1] != 15-wang-scope[2][1] \
                        and 15-zhang-scope[1][1] != 15-li-scope[3][1] \
                        and 15-wang-scope[2][1] != 15-li-scope[3][1]:
                    #将结果存入对应的数组元素
                    scope[1][2] = zhang
                    scope[1][3] = 15-zhang-7
                    scope[2][2] = wang
                    scope[2][3] = 15-wang-8
                    scope[3][2] = li
                    scope[3][3] = 15-li-9

    #打印二维数组score，输出各家孩子的分数
    print("array score:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(scope[i][j], end=' ')
        print()

    #for循环每一个孩子的分数值，并将最后一名孩子所来自的家庭保存到index中
    for n in range(len(scope)):
        #print(n, scope[n])
        for m in scope[n]:
            if m == 1:
                index = n   #记录最后一名孩子所来自的家庭
    #print(index)

    #输出最后一名孩子来自的家庭
    if index == 1:
        print("The last one reached the end is a child from family Zhang.\n")
    elif index == 2:
        print("The last one reached the end is a child from family Wang.\n")
    else:
        print("The last one reached the end is a child from family Li.\n")

