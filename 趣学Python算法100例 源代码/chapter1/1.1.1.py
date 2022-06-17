#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/1 1:22
# @desc: 抓交通肇事犯

if __name__ == "__main__":
    # i代表前两位车牌号数字，j代表后两位车牌号的数字,k代表车牌号
    i = 0
    while i <= 9:
        j = 0
        while j <= 9:
            if i != j:
                # 组成4位车牌号码
                k = i * 1000 + i * 100 + j * 10 + j
                temp = 31
                while temp <= 99:
                    if temp * temp == k:
                        print("车牌号为：", k)
                    temp += 1
            j += 1
        i += 1