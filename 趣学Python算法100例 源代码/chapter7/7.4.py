#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/24 22:55
# @desc: 人机猜数

import random


if __name__ == "__main__":
    z = random.randint(1000, 10000)  # 随机生成[1000,10000)之间的数
    # print("z = ", z)
    print("机器输入四位数：****")
    l = [0] * 4  # 存储4为随机数

    c = 1  # 变量c为猜数次数计算器
    while True:
        g = int(input("请输入你猜的四位数："))
        a = z
        j = 0  # 变量j表示数字正确的位数
        k = 0  # 变量k表示位置正确的位数
        l[0] = l[1] = l[2] = l[3] = 0
        for i in range(1, 5):  # 变量i表示原数中的第i位数。个位为第一位，千位为第4位
            s = g
            m = 1
            for t in range(1, 5):  # 人所猜想的数
                if a % 10 == s % 10:  # 若第i位与人猜的第t位相同
                    # 若该位置上的数字尚未与其他数字"相同"
                    if m and t != l[0] and t != l[1] and t != l[2] and t != l[3]:
                        j += 1
                        m = 0
                        l[j-1] = t  # 记录相同数字时，该数字在所猜数字中的位置
                    if i == t:
                        k += 1  # 若位置也相同，则计数器k加1
                s //= 10
            a //= 10
        print("你猜的结果是：%dA%dB\n" %(j, k))
        if k == 4:
            print("****** 你赢了 ******")
            break   # 若位置全部正确，则人猜对了，退出
        c += 1
    print("你总共猜了 %d 次" %c)
