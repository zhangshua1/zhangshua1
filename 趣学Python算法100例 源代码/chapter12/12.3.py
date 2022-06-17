#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/8/14 22:36
# @desc: 三色旗


#交换旗子
def SWAP(x,y):
    temp=color[x]
    color[x]=color[y]
    color[y]=temp


if __name__ == '__main__':
    WHITE = 'W'
    RED = 'R'
    BLUE = 'B'
    color = ['R', 'W', 'B', 'W', 'W', 'B', 'R', 'B', 'W', 'R'] 		#定义字符数组
    w, b, r = 0, 0, len(color)-1

    # 打印出移动前绳子上旗子的颜色
    for i in range(len(color)):
        print(color[i], end=' ')
    print()

    # 移动过程
    while w <= r:
        # 遇到的是白旗
        if color[w] == WHITE:
            w += 1  # 白旗指针自增1
        # 遇到的是蓝旗
        elif color[w] == BLUE:
            SWAP(b, w)  # 交换蓝旗指针和白旗指针所指向的旗子
            b += 1  # 蓝旗指针自增1
            w += 1  # 白旗指针自增1
        # 遇到的是红旗
        else:
            # 移动红旗指针使其指向当前最靠前的非红旗位置
            while w < r and color[r] == RED:
                r -= 1  # 红旗指针自减1
            SWAP(r, w)  # 交换红旗指针和白旗指针所指向的旗子颜色
            r -= 1  # 红旗指针自减1

    # 打印出移动后绳子上旗子的颜色
    for i in range(len(color)):
        print(color[i], end=' ')
    print()
