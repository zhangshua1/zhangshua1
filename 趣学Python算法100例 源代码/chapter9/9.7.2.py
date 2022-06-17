#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/28 1:12 
# @desc: 逆序输出字符串

# 递归函数
def rvstr(s):
    if len(s) <= 1:
        return s
    return rvstr(s[1:]) + s[0]

if __name__ == "__main__":
    str = str(input("请输入一个字符串："))
    str_result = rvstr(str)
    print("%s 逆序后： %s" % (str, str_result))