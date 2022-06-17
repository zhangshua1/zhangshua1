#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/8/14 22:51
# @desc: 农夫过河


def search(Step):
    # 若该种步骤能使各值均为1，则输出结果，进入回归步骤
    if a[Step][0] + a[Step][1] + a[Step][2] + a[Step][3] == 4:
        for i in range(Step + 1):  # 能够依次输出不同的方案
            print('east:', end=' ')
            if a[i][0] == 0:
                print('wolf', end='  ')
            if a[i][1] == 0:
                print('goat', end='  ')
            if a[i][2] == 0:
                print('cabbage', end='  ')
            if a[i][3] == 0:
                print('farmer', end='  ')
            if a[i][0] and a[i][1] and a[i][2] and a[i][3]:
                print("none", end='')
            print(end='                ')
            print('west:', end=' ')
            if a[i][0] == 1:
                print("wolf", end='  ')
            if a[i][1] == 1:
                print('goat', end='  ')
            if a[i][2] == 1:
                print('cabbage', end='  ')
            if a[i][3] == 1:
                print('farmer', end='  ')
            if not (a[i][0] or a[i][1] or a[i][2] or a[i][3]):
                print('none', end='')
            print('\n')
            if i < Step:
                print('                       the %d time' % (i + 1))
            if i>0 and i<Step:
                if a[i][3] == 0:  # 农夫在本岸
                    print("                  ----->  farmer ", end='')
                    print(name[b[i] + 1])
                else:  # 农夫在对岸
                    print("                  <-----  farmer ", end='')
                    print(name[b[i] + 1])

        print('\n\n\n')
        return

    for i in range(Step):
        if a[i] == a[Step]:  # 若该步与以前步骤相同，取消操作
            return

    # 若羊和农夫不在一起而狼和羊或者羊和白菜在一起，则取消操作
    if a[Step][1] != a[Step][3] and (a[Step][2] == a[Step][1] or a[Step][0] == a[Step][1]):
        return


    # 递归，从带第一种对象开始依次向下循环，同时限定递归的界限
    for i in range(-1, 3):
        b[Step] = i  # 记录农夫渡河方式
        a[Step+1] = a[Step][:]# 复制上一步状态，进行下一步移动
        a[Step + 1][3] = 1 - a[Step + 1][3]  # 农夫过去或者回来

        if i == -1:
            search(Step + 1)  # 进行第一步

        elif a[Step][i] == a[Step][3]:  # 若该物与农夫同岸，带回
            a[Step + 1][i] = a[Step + 1][3]  # 带回该物
            search(Step + 1)  # 进行下一步



if __name__ == '__main__':
    N = 15
    a = [[0] * 4 for i in range(N)]
    b = [0] * N

    name = ["        ",
            "and wolf",
            "and goat",
            "and cabbage"]

    print('             农夫过河问题，解决方案如下：\n')
    search(0)

