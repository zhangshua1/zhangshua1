#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/6/26 23:30
# @desc: 平方7框鱼

if __name__ == '__main__':
    print("分鱼的方案如下： ")
    count = 0
    a = [[0]*3 for i in range(3)]

    for i in range(4):  # 试探第一个人满筐a[0][0]的值，满筐数不能>3
        a[0][0] = i
        j = i
        while j <= 7 - i and j <= 3:  # 试探第二个人满筐a[1][0]的值，满筐数不能>3
            a[1][0] = j
            a[2][0] = 7 - j - a[0][0]
            j += 1
            if a[2][0] > 3:
                continue  # 第三个人满筐数不能>3
            if a[2][0] < a[1][0]:
                break  # 要求后一个人分的满筐数大于等于前一个人，以排除重复情况
            for k in range(1, 6, 2):  # 试探半筐a[0][1]的值，半筐数为奇数
                a[0][1] = k
                for m in range(1, 7 - k, 2):  # 试探半筐a[1][1]的值，半筐数为奇数
                    a[1][1] = m
                    a[2][1] = 7 - k - m
                    # 判断每个人分到的鱼是 3.5筐，flag为满足题意的标记变量
                    flag, n = True, 0
                    while flag and n < 3:
                        if a[n][0] + a[n][1] < 7 and a[n][0] * 2 + a[n][1] == 7:
                            a[n][2] = 7 - a[n][0] - a[n][1]  # 计算应得到的空筐数量
                        else:
                            flag = False  # 不符合题意则置标记为0
                        n += 1

                    if flag:
                        count += 1
                        print('No.', count, ' Full basket Semi-basket Empty')
                        for n in range(3):
                            print('fisher ', chr(65 + n), ':', a[n][0], a[n][1], a[n][2])

