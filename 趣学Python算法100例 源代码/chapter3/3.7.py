#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/11 23:18 
# @desc: 高次方数的尾数

if __name__ == "__main__":
    last = 1  # 变量last保存求得的x的y次方的部分积的后三位
    print("请输入两个数x和y：")
    x = int(input("x = "))
    y = int(input("y = "))
    for i in range(1, y+1):
        last = last * x % 1000  # 将last乘x后对1000取模，即求积的后三位
    print("%d的%d次方所得积的后三位为：%d" %(x,y,last))