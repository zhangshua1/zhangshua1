#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/27 23:23
# @desc: 猴子吃桃

# 递推公式：A(n) = (A(n+1) + 1) * 2
def A(n):
    if n >= 9:
        return 1  # 递归出口
    else:
        return (2 * (A(n+1) + 1))   # 递推公式


if __name__ == "__main__":
    print("猴子第一天总共摘了 %d 个桃子" %A(0))
