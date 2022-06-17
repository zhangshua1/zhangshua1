#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/19 0:22
# @desc: 歌星大奖赛

import random

# 求出最大分数值
def maxScore(score):
    max = score[0]  # 给max赋初值
    m = 0  # m记录最大值的下标
    for j in range(1, 10):
        if max < score[j]:
            max = score[j]
            m = j  # 记录最大值的下标
    print("最大的分数为：%d" % max)
    return max,m

# 求出最小分数值
def minScore(score):
    min = score[0]  # 给min赋初值
    n = 0  # n记录最小值的下标
    for j in range(1, 10):
        if min > score[j]:
            min = score[j]
            n = j  # 记录最小值的下标
    print("最小的分数为：%d" % min)
    return min,n


if __name__=="__main__":
    sum = 0   # 记录10个评委打分的总分数
    score = [0]*10
    for i in range(10):
        score[i] = random.randint(0, 101)  # 生成10个随机分数
        sum = sum + score[i]
    print("10个评委的打分为：", score)
    max,m = maxScore(score)
    min,n = minScore(score)

    avg = (sum - max - min) // 8  # 计算平均分
    print("去掉最高分和最低分，最后得分：%d" %avg)

    temp = 0  # temp用来记录最公平与最不公平评委给出的评分存储的下标
    s = abs(score[0] - avg)  # s记录评分与平均值差的绝对值
    for i in range(10):
        if abs(score[i] - avg) == 0:
            temp = i
            print("最公平的评委是：%d, 打分：%d" % ((temp + 1),(score[temp+1])))

    temp = 0
    for i in range(10):
        if abs(score[i] - avg) != 0:
            if s > abs(score[i] - avg):
                s = abs(score[i] - avg)
                temp = i
    print("最公平的评委是：%d" %(temp + 1))

    if (avg - min) == (max - avg):
        print("最不公平的评委是：%d %d" %((m+1), (n+1)))
    else:
        if (avg - min) > (max - avg):
            print("最不公平的评委就是：%d" %(n+1))
        else:
            print("最不公平的评委就是：%d" %(m+1))
