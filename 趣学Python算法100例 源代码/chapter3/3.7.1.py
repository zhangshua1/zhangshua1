#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/11 23:28 
# @desc: 高次方数的尾数

if __name__ == "__main__":
    last = 1  # 变量last保存求得的x的y次方的部分积的后三位
    for i in range(1, 13+1): # x自乘的次数
        last = last * 13 % 1000 # 将last乘x后对1000取模，即求积的后三位
    print("13的13次方所得积的后三位为：%d" %last)