#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/30 0:30
# @desc: 回文数的形成
# 任取一个十进制正整数，将其倒过来后与原来的正整数相加，会得到一个新的正整数。重复以上步骤，则最终可得到一个回文数。

# 求反序数
def reverse(a):
    t = 0
    while a > 0:
        t = t * 10 + a % 10  # t中存放的是a的反序数
        a //= 10
    return t

# 判断是否为回文数
def palindrome(s):
    if (reverse(s) == s):  # 调用reverse函数判断变量s是否与其反序数相等
        return 1  # s是回文数则返回1
    else:
        return 0  # s不是回文数返回0


if __name__ == '__main__':
    #与c语言不同的是，python支持大数计算，无限位数。
    # 对于小整数，它会使用机器自身的整数计算功能去快速计算，当超出机器自身所能支持的范围的时候，自动转换大数计算。
    n = int(input("请输入一个正整数："))
    print("回文数的产生过程如下：")
    count = 0
    m = reverse(n)
    while (palindrome(m + n) == 0):  # 判断当前的整数n是否为回文数
        count += 1
        print("[%d]:%d+%d=%d " % (count, n, m, m + n))  # 打印操作步骤
        n += m  # n加上其反序数
        m = reverse(n)
    count += 1
    print("[%d]:%d+%d=%d\n" % (count, n, m, m + n))






