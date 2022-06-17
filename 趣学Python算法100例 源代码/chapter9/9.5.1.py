#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 23:04
# @desc: 递归解决分鱼问题

if __name__ == "__main__":
    # fish[6]存放每个人分鱼前的总条数
    fish = [0]*6  # A、B、C、D、E分鱼前鱼的总条数分别存放在fish数组下标为1、2、3、4、5的元素中。
    fish[5] = 6
    while True:
        i = 4
        while i > 0:
            if fish[i+1] % 4 != 0:
                break
            fish[i] = fish[i+1] * 5 // 4 + 1  # 地推关系式
            if fish[i] % 5 != 1:
                break
            i -= 1
        if i == 0:
            break
        fish[5] += 5
    for i in range(1, 6):
        print("fish[%d] = %d " %(i, fish[i]))  # 输出结果
