#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/7 1:14
# @desc: 常胜将军

if __name__ == "__main__":
    spare = 21  # 21根火柴
    print("--------你不能战胜我，不信试试--------")
    print("开始游戏: ")
    while 1:
        print("--------目前还有火柴 %d 根--------" %spare)
        people = int(input("人取火柴："))   # 人取火柴
        if people < 1 or people > 4 or people > spare:
            print("你违规了，你取的火柴数有问题！")
            continue
        spare = spare - people   # 人取后，剩余的火柴数
        if spare == 0:   # 人取后，剩余的火柴数为0， 则计算机获胜，跳出循环
            print("计算机获胜，游戏结束！")
            break
        computer = 5 - people   # 计算机取火柴
        spare = spare - computer
        print("计算机取火柴：%d" %computer)
        # 计算机取后，剩余的火柴数为0， 则人获胜，跳出循环
        if spare == 0:
            print("人获胜，游戏结束！")
            break