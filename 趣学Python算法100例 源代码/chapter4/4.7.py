#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/17 2:23 
# @desc: 分数比较

# 求两个数的最大公约数
def common_divisor(a, b):
    # 若a < b，则交换两变量的值
    if a < b:
        temp = a
        a = b
        b = temp
    # 求分母a, b的最大公约数
    c = a * b
    while b != 0:
        d = b
        b = a % b
        a = d
    return c // a


if __name__ == "__main__":
    print("请分别输入两个分数：")
    i, j = [int(i) for i in input("请输入第一个分数: ").split()]
    k, l = [int(i) for i in input("请输入第二个分数: ").split()]
    print("第一个分数：%d/%d" %(i, j))
    print("第二个分数：%d/%d" %(k, l))
    m = common_divisor(j, l) // j * i  # 求出第一个分数通分后的分子
    n = common_divisor(j, l) // l * k  # 求出第二个分数通分后的分子
    if m > n:
        print("%d/%d > %d/%d" %(i,j,k,l))
    else:
        if m == n:
            print("%d/%d = %d/%d" %(i,j,k,l))
        else:
            print("%d/%d < %d/%d" %(i,j,k,l))
