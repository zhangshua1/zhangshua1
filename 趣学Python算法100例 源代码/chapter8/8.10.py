#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/27 20:12 
# @desc: 指定位置插入字符

def insert_str(s):
    a = [0] * len(s)
    for i in range(len(s)):  # 遍历字符串
        a[i] = s[i]   # 将字符串存入列表数组

    # 遍历数组元素
    for i in a:
        # 用isdigit函数判断是否数字
        flag = i.isdigit()  # 是数字返回True
        if flag == True:
            i = '$'+i
        print(i, end="")

if __name__=="__main__":
    s = str(input("请输入一个字符串："))
    print("输入的字符串为：", s)
    insert_str(s)
