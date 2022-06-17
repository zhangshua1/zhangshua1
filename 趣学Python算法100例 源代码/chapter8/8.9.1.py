#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/11 1:43 
# @desc: 删除“*”号  正则法

import re

# 删除指定位置的 * 号
def fun(s):
    result_str = re.sub(r'([a-zA-Z]+)(.+)([a-zA-Z]+)', lambda match: ''.join([m.replace('*', '') for m in match.groups()]), s)
    print(result_str)

if __name__ == "__main__":
    s = str(input("请输入一个只包含字母和*号的字符串：\n"))
    print("输入的字符串为：", s)
    fun(s)