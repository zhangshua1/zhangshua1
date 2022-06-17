#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author:liuhefei
# desc: 委派任务

if __name__ == "__main__":
    # A、B、C、D、E、F 可能取值分别 0 或 1,  (0: 不去, 1: 去)
    # 穷举所有情况
    for A in range(2):
        for B in range(2):
            for C in range(2):
                for D in range(2):
                    for E in range(2):
                        for F in range(2):
                            # 逻辑表达式作为判断条件
                            if (A + B >= 1) and (A + D != 2) and (A + E + F == 2) and (
                                    (B + C == 0) or (B + C == 2)) and (C + D == 1) and ((D + E == 0) or D == 1):
                                a = '' if A == 1 else "未"  # 三元表达式
                                print("A" + a + "被选择去完成任务。")

                                b = '' if B == 1 else "未"
                                print("B" + b + "被选择去完成任务。")

                                c = '' if C == 1 else "未"
                                print("C" + c + "被选择去完成任务。")

                                d = '' if D == 1 else "未"
                                print("D" + d + "被选择去完成任务。")

                                e = '' if E == 1 else "未"
                                print("E" + e + "被选择去完成任务。")

                                f = '' if F == 1 else "未"
                                print("F" + f + "被选择去完成任务。")

