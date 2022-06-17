#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 23:09
# @desc: 汉诺塔问题

def hanoi(N, A, B, C):
    if N == 1:   # 将A座上剩下的第N个盘子移动到C座上
        print("move dish %d from %c to %c " %(N, A, C))  # 打印移动步骤
    else:
        hanoi(N-1, A, C, B)  # 借助C座将N-1个盘子从A座移动到B座
        print("move dish %d from %c to %c " %(N, A, C))  # 打印移动步骤
        hanoi(N-1, B, A, C)


if __name__ == "__main__":
    n = int(input("Please input the number of dishes："))   #输入要移动的盘子个数
    print("The steps to move %2d dishes are: " %n);
    hanoi(n, 'A', 'B', 'C'); # 调用递归函数
