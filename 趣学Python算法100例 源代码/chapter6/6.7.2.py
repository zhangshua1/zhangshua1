#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author:liuhefei
#desc: 谜语博士的难题(一)

if __name__=="__main__":
    # 分别使用A,B,C代表第一个，第二个，第三个人， 说谎对应的变量值为0，诚实对应的变量值为1
    for A in range(2):
        for B in range(2):
            for C in range(2):
                #使用多个if语句判断
                if (A and A + B + C == 2) or (not A and A + B + C != 2):
                    if(B and A + B + C == 1) or (not B and A + B + C != 1):
                        if(C and A + B + C == 1) or (not C and A + B + C != 1):
                            if A == 0:
                                a = "说谎族"
                            else:
                                a = "诚实族"
                            if B == 0:
                                b = "说谎族"
                            else:
                                b = "诚实族"
                            if C == 0:
                                c = "说谎族"
                            else:
                                c = "诚实族"
                            #print(A,B,C)
                            print("第一个人来自" + a)
                            print("第二个人来自" + b)
                            print("第三个人来自" + c)


