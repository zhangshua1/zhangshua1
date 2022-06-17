#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/14 1:40 
# @desc: 不重复的3位数

if __name__=="__main__":
    count = 0 # 计数器
    for i in range(1, 5):
        for j in range(1, 5):
            k = 1
            while k < 5 and j != i:
                if k != j and k != i:
                    print("%d%d%d  " %(i,j,k), end=" ")
                    count += 1
                    if count % 8 == 0:   # 每输出8个换一行
                        print()
                k += 1
    print("三位互不相同的数，共有：%d" % count, "个")