#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author:liuhefei
#desc: 谜语博士的难题(一)

if __name__ == "__main__":
    #分别使用A,B,C代表第一个，第二个，第三个人， 说谎对应的变量值为0，诚实对应的变量值为1
    for A in range(2):
        for B in range(2):
            for C in range(2):
                #逻辑判断条件
                if ((A and A + B + C == 2) or (not A and A + B + C != 2)) \
                        and ((B and A + B + C == 1) or (not B and A + B + C != 1))  \
                        and ((C and A + B + C == 1) or (not C and A + B + C != 1)):
                    a = "诚实族" if A else "说谎族"
                    b = "诚实族" if B else "说谎族"
                    c = "诚实族" if C else "说谎族"
                    print("第一个人来自" + a )
                    print("第二个人来自" + b)
                    print("第三个人来自" + c)
