#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/11 22:12
# @desc: 回文数

if __name__ == '__main__':
    m = [1] * 17
    count = 0
    print("No.    number     it's square(palindrome)")
    for n in range(1, 256):            # 穷举n的取值范围
        k, i, t, a = 0, 0, 1, n*n         # 计算n的平方
        squ = a
        while a != 0:    		    # 从低到高分解数a的每一位存于数组m[1]~m[16]
            m[i] = a % 10
            a //= 10
            i += 1

        while i > 0:
            k += m[i-1] * t   			# t记录某一位置对应的权值
            t *= 10
            i -= 1

        if k == squ:
            count += 1
            print("%2d%10d%10d" % (count, n, n*n))
