#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author: liuhefei
#desc: 谁在说谎

if __name__ == "__main__":
    # x、y和z分别表示张三、李四和王五三人说话真假的情况
    # 当x、y或z的值为1时表示该人说的是真话，值为0时表示该人说的是假话
    #使用三重循环穷举所有情况、
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (x and (not y) or (not x) and y) and (y and (not z) or (not y) and z) and (z and x ==0 and y==0 or (not z) and x+y != 0):
                    a = '真' if x == 1 else '假'
                    b = '真' if y == 1 else '假'
                    c = '真' if z == 1 else '假'
                    print("张三说的是" + a + "话")
                    print("李四说的是" + b + "话")
                    print("王五说的是" + c + "话")