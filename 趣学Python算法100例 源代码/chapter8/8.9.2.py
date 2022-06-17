#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/10 23:41 
# @desc: 删除“*”号
"""
实例：输入： ****A*BC*DEF*G********
     输出： ****ABCDEFG********
"""

def fun(s):
    a = [0] * len(s)
    for i in range(len(s)):
        a[i] = s[i]  # 将字符串拆分存入数组
    print("结果：", end="")
    for j in a:
        if j == '*':
            j = ""
        print(j, end="")


if __name__ == "__main__":
    s = str(input("请输入一个只包含字母和*号的字符串：\n"))
    print("输入的字符串为：", s)
    fun(s)