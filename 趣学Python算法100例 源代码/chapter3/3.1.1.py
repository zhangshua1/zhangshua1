#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/11 22:35
# @desc: 回文数


if __name__ == '__main__':
    x = int(input("请输入一个5位数整数："))
    if x < 10000 or x > 99999:
        print("输入错误")
    else:
        ten_thousand = x // 10000   #拆分最高位万位
        thousand = x % 10000 // 1000		# 拆分千位
        ten = x % 100 // 10			#拆分十位
        indiv = x % 10			#拆分个位
        if indiv == ten_thousand and ten == thousand:
            print("%d是回文数" %x)
        else:
          print("%d不是回文数" %x)