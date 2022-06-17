#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/5/30 0:16
# @desc: 借书方案知多少

if __name__=="__main__":
    #A,B,C三位小朋友，5本书，每人每次只能借一本
    #用a,b,c分别表示三人所选新书编号
    i = 0  # i表示有效借阅次数
    print("A,B,C三人所选书号分别为：")
    #用来控制A借阅图书编号
    for a in range(1, 6):
        #用来控制B借阅图书编号
        for b in range(1, 6):
            #用来控制C借阅图书编号
            for c in range(1, 6):
                if a != b and a != c and c != b:
                    print("A:%2d  B:%2d  C:%2d    " %(a, b, c) ,  end='')
                    i += 1
                    if i % 4 == 0:
                        print()  #换行
    print("共有%d种有效借阅方法" %i)