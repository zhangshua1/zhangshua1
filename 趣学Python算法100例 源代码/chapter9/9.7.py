#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/28 0:37 
# @desc:  逆序输出数字

# 逆序函数
def reverse(n):
    if n != 0:
        print("%d" % (n % 10), end="")  # 输出正整数n当前的最高位
        reverse(n // 10)  # 递归调用

if __name__ == "__main__":
    num = int(input("请输入一个整数："))
    # 如果num小于0，就先把num转化字符串，截取第一位 -号，然后将数字逆序，在拼接上符号输出
    if num < 0:
        str_num = str(num)
        num = str_num[1:]  # 剪切掉符号位
        print("-", end="")
        reverse(int(num))
    else:
        reverse(num)
