#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/5/30 1:05
# @desc: 借书方案知多少

if __name__=="__main__":
    # A,B,C三位小朋友，5本书，每人每次只能借一本
    # 用a,b,c分别表示三人所选新书编号
    i = 0  # i表示有效借阅次数
    print("A,B,C三人所选书号分别为：")
    a = 1
    while a <= 5:
        b = 1
        while b <= 5:
            c = 1
            while c <= 5 and a != b:
                if a != c and b != c:  # 控制有效借阅组合
                    print("A:%2d  B:%2d  C:%2d    " % (a, b, c), end='')
                    i += 1
                    if i % 4 == 0:
                        print()  # 换行
                c += 1
            b += 1
        a += 1

    print("共有%d种有效借阅方法" % i)
