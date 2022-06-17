#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/13 10:16
# @desc: 自动发牌


import random

def p(b, n):
    print("\n♠ ", end='')  # 打印黑桃标记
    for i in range(13):  # 将数组中的值转换为相应的花色
        if b[i] // 13 == 0:  # 找到该花色对应的牌
            print(n[b[i] % 13], end=' ')

    print("\n♥ ", end='')  # 打印红桃标记
    for i in range(13):
        if b[i] // 13 == 1:
            print(n[b[i] % 13], end=' ')

    print("\n♦ ", end='')  # 打印方块标记
    for i in range(13):
        if b[i] // 13 == 2:
            print(n[b[i] % 13], end=' ')

    print("\n♣ ", end='')  # 打印梅花标记
    for i in range(13):
        if b[i] // 13 == 3 or b[i] // 13 == 4:
            print(n[b[i] % 13], end=' ')

    print()


if __name__ == '__main__':
    n = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    a = [0] * 53
    b1 = [0] * 13
    b2 = [0] * 13
    b3 = [0] * 13
    b4 = [0] * 13

    b11, b22, b33, b44, t = 0, 0, 0, 0, 1
    while (t <= 52):  # 控制发52张牌
        m = random.randint(0, 52)  # 产生0到51之间的随机数
        flag, i = True, 1
        while i <= t and flag:  # 查找新产生的随机数是否已经存在
            if m == a[i]:
                flag = 0  # flag = 1表示产生的是新的随机数，flag = 0 表示新产生的随机数已经存在
            i += 1

        if flag:
            a[t] = m  # 如果产生了新的随机数，则存入数组
            t += 1
            # 根据t的模值，判断当前的牌应存入哪个数组中
            if t % 4 == 0:
                b1[b11] = a[t - 1]
                b11 += 1

            elif t % 4 == 1:
                b2[b22] = a[t - 1]
                b22 += 1

            elif t % 4 == 2:
                b3[b33] = a[t - 1]
                b33 += 1

            elif t % 4 == 3:
                b4[b44] = a[t - 1]
                b44 += 1


    b1 = sorted(b1, reverse=True)  # 将每个人的牌进行排序
    b2 = sorted(b2, reverse=True)
    b3 = sorted(b3, reverse=True)
    b4 = sorted(b4, reverse=True)

    p(b1, n)  # 分别打印每个人的牌
    p(b2, n)
    p(b3, n)
    p(b4, n)

