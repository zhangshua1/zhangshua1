#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/5 1:27 
# @desc:  猜牌术

if __name__ == '__main__':
    a = [0] * 14  # 初始化列表，用来存放13张牌
    j = 1  # j是数组的下标，空盒子的序号
    print("魔术师手中的牌原始次序是:")
    #外循环13次，每次将一张牌放入空盒中
    for i in range(1, 14): # i表示牌的序号
        # n用来记录当前的空盒序号，初值为1
        n = 1           # 每次都从一个空盒开始重新计数
        while n <= i:
            if j > 13:
                j = 1
            if a[j]:    # 盒子非空，跳过该盒子
                j += 1
            else:
                if n == i:  # 判断该盒子是否为第i个空盒
                    a[j] = i  # 是则将i存入
                j += 1
                n += 1

    print(a[1:])
