#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/7/7 11:45
# @desc: 填表格   2行3列的表格


# 判断a[1]-a[4]的取值
def judge(b):
    for i in range(1, 4):
        l = i + 1
        while l < 5:
            if (b[l] == b[i]):
                return False  # 判断a[1]~ a[4]的取值是否有重复，若有重复则返回flase
            l += 1

    return True  # 若a[1]~ a[4]的取值各不相同，则返回True


if __name__ == '__main__':
    count = 1                  # 计数器
    a = [1, 2, 3, 4, 5, 6]              # 初始化列表
    print("满足条件的结果为:")
    a[1] = a[0] + 1
    while a[1] <= 5:         # a[1]必须大于a[0]
        a[2] = a[1] + 1
        while a[2] <= 5:    # a[2]必须大于a[1]
            a[3] = a[0] + 1
            while a[3] <= 5:  # 第二行的a[3]必须大于a[0]
                              # 第二行的a[4]必须大于左侧a[3]和上边a[1]
                if a[1] > a[3]:
                    a[4] = a[1] + 1
                else:
                    a[4] = a[3] + 1
                while a[4] <= 5:
                    if judge(a):    # 如果满足题意，打印结果
                        print("结果%d:" % count)
                        count += 1
                        print(a[:3])
                        print(a[3:])
                        print()
                    a[4] += 1
                a[3] += 1
            a[2] += 1
        a[1] += 1

