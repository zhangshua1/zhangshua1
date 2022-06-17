#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author:liuhefei
#desc: 旅客国际


country = [" ", "美国", "英国", "法国", "德国", "意大利", "俄罗斯"]   #国名

def Nationality():
    #初始化条件矩阵
    a = []
    for i in range(7):
        b = []
        for j in range(7):
            b.append(j)
        a.append(b)

    for i in range(1, 7):   #条件矩阵每一列的第0号元素作为该列数据处理的标记
        a[0][i] = 1         #标记该列尚未处理

    a[1][1] = a[2][1] = a[3][1] = a[5][1] = 0  #输入条件矩阵中的各种条件
    a[1][3] = a[2][3] = a[3][3] = 0     #0表示不是该国人
    a[1][4] = a[2][4] = a[3][4] = a[5][4] = a[6][4] = 0
    a[3][5] = 0
    a[1][6] = a[3][6] = a[5][6] = 0

    x = 0
    y = 0
    while a[0][1] + a[0][2] + a[0][3] + a[0][4] + a[0][5] + a[0][6] > 0:
        #当所有六列均处理完毕后退出循环
        for i in range(1, 7):  #i为列坐标
            if a[0][i] != 0:   #若该列尚未处理，则进行处理
                e = 0
                for j in range(1, 7):  #j变量保存行坐标，e变量是该列中非0元素计数器
                    if a[j][i] != 0:
                        #统计每列中的非0元素个数
                        x = j   #x变量保存行坐标
                        y = i   #y变量保存列坐标
                        e += 1
                if e == 1:       #若该列只有一个元素为非零，则进行消去操作
                    for t in range(1, 7):
                        if t != i:
                            a[x][t] = 0   #将非零元素所在的行的其他元素置0
                    a[0][y] = 0      #设置该列已处理完毕的标记

    print("矩阵最终状态为：")
    #输出执行消去操作后矩阵的最终状态
    for i in range(7):
        print(a[i])

    print("推断结果为：")
    for i in range(1, 7):
        print(chr(ord('A') - 1 + i), '来自: ', end='')
        for j in range(1, 7):
            if a[i][j] != 0:
                print(country[a[i][j]], '。')
                break


if __name__ == '__main__':
    Nationality()






