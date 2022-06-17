#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/14 1:34 
# @desc: 不重复的3位数

if __name__ == "__main__":
    count = 0   # 计数器
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != k and i != j and j != k:   # 判断三个数是否互不相同
                    count += 1
                    print("%d%d%d  " %(i,j,k), end=" ")
                    if count % 8 == 0:
                        print()
    print("三位互不相同的数，共有：%d" %count, "个")