#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author:liuhefei
#desc: 黑与白

if __name__=="__main__":
    #A、B、C、D、E五个人，每个人额头上都帖了一张黑或白的纸
    #变量a、b、c、d、e分别代表A、B、C、D、E五个人额头上贴纸的颜色，
    # 当变量的取值为1时表示该人额头上贴纸为白色，当变量取值为0时表示该人额头上贴纸为黑色
    for a in range(2):  #a,b,c,d,e变量值要么为0，要么为1，0为黑色，1为白色
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        if (a and (b + c + d + e == 3) or ((not a) and (b + c + d + e != 3))):   #A
                            if(b and (a + c + d + e == 0) or ((not b) and (a + c + d + e != 0))):  #B
                                if(c and (a + b + d + e == 1) or ((not c) and (a + b + d + e != 1))): #C
                                    if (d and (a + b + c + e == 4) or ((not d) and (a + b + c + e != 4))): #D
                                        a1 = "白" if a==1 else "黑"    #三元表达式
                                        b1 = "白" if b==1 else "黑"
                                        c1 = "白" if c==1 else "黑"
                                        d1 = "白" if d==1 else "黑"
                                        e1 = "白" if e==1 else "黑"
                                        print("A额头上的贴纸是" + a1 + "色的.")
                                        print("B额头上的贴纸是" + b1 + "色的.")
                                        print("C额头上的贴纸是" + c1 + "色的.")
                                        print("D额头上的贴纸是" + d1 + "色的.")
                                        print("E额头上的贴纸是" + e1 + "色的.")
