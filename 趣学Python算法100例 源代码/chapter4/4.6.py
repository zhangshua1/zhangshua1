#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/17 1:24
# @desc: 歌星大奖赛


if __name__ == "__main__":
    max = 0
    min = 100
    sum = 0   # sum存放10个评委打分的总分数
    for i in range(1, 11):
        print("第%d个评委打分：" %i, end="")
        integer = int(input())  # 输入评委的评分
        if integer < 0 or integer > 100:  # 对分数值进行验证
            print("输入的分数错误")
            exit()
        sum += integer  # 计算总分
        if integer > max:  #通过比较筛选出其中的最高分
            max = integer
        if integer < min:  #通过比较筛选出其中的最低分
            min = integer
    print("去掉一个最高分：%d" % max)
    print("去掉一个最低分：%d" % min)
    print("最后得分：%d" % ((sum - max - min) // 8))