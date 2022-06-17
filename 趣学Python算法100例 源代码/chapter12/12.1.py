#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/8/14 22:23
# @desc: 约瑟夫环


if __name__ == '__main__':
    array = [[0] * 2 for i in range(31)]  # 30个人，0号元素没有使用
    print('最终结果为(s:被扔下海,b:在船上):')
    for i in range(1, 31):  # 初始化结构数组
        array[i][0] = 1  # flag标志置为1，表示人在船上
        array[i][1] = i + 1  # next值为数组中下一个元素的下标，即指向下一个人
    array[30][1] = 1  # 第30个人的数组下标指向第一个人以构成环
    j = 30  # 变量j指向已经处理完毕的数组元素，从array[i]指向的人开始计数
    for i in range(15):  # 循环变量i作为计数器，记录已扔下海的人数，共15个人
        k = 0
        while True:  # 循环变量k:作为计数器，决定哪个人被扔下海，计数到9为止
            if k < 9:
                j = array[j][1]  # 修改数组下标，取下一个人
                k += array[j][0]  # 进行计数。已扔下海的人标记为0
            else:
                break  # 计数到9则停止计数
        array[j][0] = 0  # 将标记置 0，表示该人已被扔下海

    for i in range(1, 31):  # 输出结果
        if array[i][0]:
            print('b', end='')
        else:
            print('s', end='')
    print()

