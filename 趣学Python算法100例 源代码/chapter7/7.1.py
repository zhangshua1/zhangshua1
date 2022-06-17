#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/13 10:07
# @desc: 黑白子交换

# 打印输出结果
def printLine(a):
    global number

    print("No. %2d:……………………….." % number)
    number += 1
    print(" ", end='')

    for i in range(7):
        if a[i] == 1:
            print('| * ', end='')
        else:
            if a[i] == 2:
                print('| @ ', end='')
            else:
                print('|  ', end='')
    print(" |\n ………………………..")

# 交换
def change(t, i, j):
    term = t[i]
    t[i] = t[j]
    t[j] = term
    return t


if __name__ == '__main__':
    t = [1, 1, 1, 0, 2, 2, 2]  # 初始化数组 1：白子 2：黑子 0：空格
    number = 0
    printLine(t)
    # 若还没有完成棋子的交换则继续进行循环
    while t[0] + t[1] + t[2] != 6 or t[4] + t[5] + t[6] != 3:  # 判断游戏是否结束
        # flag为棋子移动一步的标记，flag=True表示尚未移动棋子，flag=Flase表示已经移动棋子
        flag = True

        i = 0
        while flag and i < 5:  # 若白子可以向右跳过黑子，则白子向右跳
            if t[i] == 1 and t[i + 1] == 2 and t[i + 2] == 0:
                t = change(t, i, i + 2) # 调用交换
                printLine(t)
                flag = False
            i += 1

        i = 0
        while flag and i < 5:  # 若黑子可以向左跳过白子，则黑子向左跳
            if t[i] == 0 and t[i + 1] == 1 and t[i + 2] == 2:
                t = change(t, i, i + 2)
                printLine(t)
                flag = False
            i += 1

        i = 0
        while flag and i < 6:  # 若向右移动白子不会产生阻塞,则白子向右移动
            f = True
            if i < 5:
                f = t[i - 1] != t[i + 2]
            if t[i] == 1 and t[i + 1] == 0 and (i == 0 or f):
                t = change(t, i, i + 1)
                printLine(t)
                flag = False
            i += 1

        i = 0
        while flag and i < 6:  # 若向左移动黑子不会产生阻塞，则黑子向左移动
            f = True
            if i < 5:
                f = t[i - 1] != t[i + 2]
            if t[i] == 0 and t[i + 1] == 2 and (i == 5 or f):
                t = change(t, i, i + 1)
                printLine(t)
                flag = False
            i += 1
