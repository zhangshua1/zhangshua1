#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/1 22:42 
# @desc: 最佳存款方案

if __name__=="__main__":
    i = 0
    money = 0.0
    while i < 5:
        money = (money + 1000)/(1 + 0.0063 * 12)
        i += 1
    print("应该存入钱数为：%0.2f" %money)   # 结果保留两位小数