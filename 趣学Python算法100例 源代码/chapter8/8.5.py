#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/26 22:03
# @desc: 选美比赛

#应用冒泡排序法，排序后的数组psn按照score的值从小到大排列
def sortScore(psn, n):
   for i in range(n-1):
    for j in range(n-1-i):
        if psn[j][1] > psn[j+1][1]:
            #交换psn[j]与psn[j+1]
            tmp = psn[j]
            psn[j] = psn[j+1]
            psn[j+1] = tmp


#指定每一位选手的名次
def setRand(psn, n):
    j = 1
    psn[0][2] = 1  # 设定第一位选手的名次
    for i in range(n):   # 设定psn[2]～psn[n-1]的名次
        if psn[i][1] != psn[i-1][1]:
            psn[i][2] = j
            j += 1
        else:
            psn[i][2] = psn[i-1][2]  # psn[i]与psn[i-1]的名次相同


#最后再按照选手的序号重新排序，以便能够按照选手的序号输出结果
def sortNum(psn, n):
   for i in range(n-1):
    for j in range(n-1-i):
        if psn[j][0] > psn[j+1][0]: #交换psn[j]与psn[j+1]
            tmp = psn[j]
            psn[j] = psn[j+1]
            psn[j+1] = tmp


def sortRand(psn, n):
    sortScore(psn, n)          #以分数为关键字排序
    setRand(psn, n)           #按照分数排名次
    sortNum(psn, n)           #按照序号重新排序


if __name__ == '__main__':
   #选手的信息组成一个结构体数组
    psn = [[1, 5, 0], [2, 3, 0], [3, 4, 0], [4, 7, 0], [5, 3, 0], [6, 5, 0], [7, 6, 0]]
    sortRand(psn, 7)
    print("num   score rand  ")
    #输出结果
    for i in range(7):
        print("%d%6d%6d" % (psn[i][0], psn[i][1], psn[i][2]))

