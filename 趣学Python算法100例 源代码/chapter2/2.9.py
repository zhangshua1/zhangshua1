#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/6 0:23 
# @desc: 舍罕王的失算

if __name__=="__main__":
    # 使用循环求累加和
    i = 1
    sum = 0.0
    while i <= 64:
        sum = sum + 2**(i-1)
        # print("sum" , i , "=" , sum)
        i += 1
    print("国王总共需要赏赐给宰相的麦子数为：\n%f\n" %sum)   # 打印结果

