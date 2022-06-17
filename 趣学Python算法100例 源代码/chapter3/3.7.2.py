#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/11 23:33 
# @desc: 高次方数的尾数

#思路：求出x的y次方的积，转换为字符串，然后截取后三位

if __name__ == "__main__":
    print("请输入两个数x和y：")
    x = int(input("x = "))
    y = int(input("y = "))
    xy = pow(x, y)   # xy 为 x 的 y次方的乘积，等价于 x**y
    print("x的y次方的积：", xy)
    str_xy = str(xy)   # 将xy转换为字符串
    # 截取字符串的后三位
    str_result = str_xy[-3: ]
    print("x的y次方的积的后三位为：", str_result)