#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/25 0:08
# @desc: 搬山游戏


if __name__ == "__main__":
    print("More Mountain Game")
    print("Game Begin")
    pc = cc = 0
    g = 1
    while True:
        print("No.%2d game " %g)
        print("---------------------")
        print("How many mountains are there? ", end="")
        n = int(input())  # 输入山的总数
        if not n:
            break

        k = int(input("How many mountains are allowed to each time? "))   # 允许的搬山数
        while(k > n or k < 1):
            if k > n or k < 1:
               print("Repeat again!")

        while n:
            x = int(input("How many mountains do you wish move away? "))
            if x < 1 or x > k or x > n:  # 判断搬山数是否符合要求
                print("IIIegal,again please!")
                continue;
            n -= x
            print("There are %d mountains left now." %n)
            if not n:
                print("……………I win. You are failure……………")
                cc += 1
            else:
                y = (n-1) % (k+1)   # 求出最佳搬山数
                if not y:
                    y = 1
                n -= y
                print("Copmputer move %d mountains away." %y)
                if n:
                    print(" There are %d mountains left now."  %n)
                else:
                    print("……………I am failure. You win………………")
                    pc += 1
        g += 1

    # 打印结果
    print("Games in total have been played %d." %(cc + pc))
    print("You score is win %d,lose %d." %(pc, cc))
    print("My score is win %d,lose %d." %(cc, pc))




