#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author:liuhefei
#desc: 谜语博士的难题(二)

if __name__=="__main__":
    #分别使用变量L,M,R表示左边,中间,右边的人来自诚实族
    #分别使用变量LL,MM,RR表示左边,中间,右边的人来自两面族
    #0表示说谎，1表示诚实
    for L in range(2):   #穷举
        for M in range(2):
            for R in range(2):
                for LL in range(2):
                    for MM in range(2):
                        for RR in range(2):
                            if ((L and (not LL) and M and (not MM)) or ((not L) and (not M)) and (not M)):
                                if ((R and (not M) and (not MM) or (RR and (not R))) or ((not R) and (not RR) and (M or MM))):
                                    if ((L + LL != 2) and (M + MM != 2) and (R + RR != 2) and (L + M + R == 1) and (LL + MM + RR == 1)):
                                        # 使用三元表达式
                                        l = "两面族" if LL else ("诚实族" if L else "说谎族")
                                        m = "两面族" if MM else ("诚实族" if M else "说谎族")
                                        r = "两面族" if RR else ("诚实族" if R else "说谎族")
                                        print("左边的人来自" + l)
                                        print("中间的人来自" + m)
                                        print("右边的人来自" + r)
