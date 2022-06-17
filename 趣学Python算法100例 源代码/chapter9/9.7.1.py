#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/28 1:08 
# @desc: 逆序输出字符串

def reverse_string(s):
    if len(s) > 1:
        reversed_s = ''.join(reversed(s))
        return reversed_s
    return s

if __name__ == "__main__":
    str = str(input("请输入一个字符串："))
    str_result = reverse_string(str)
    print("%s 逆序后： %s" %(str, str_result))