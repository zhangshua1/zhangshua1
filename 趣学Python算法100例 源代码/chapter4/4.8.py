#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/6/18 0:15 
# @desc: 计算分数精确值

if __name__ == "__main__":
    remainder = [0]*101   # remainder存放除法的余数
    quotient = [0]*101    # quotient 依次存放商的每一位
    print("请输入分子与分母大于0，小于等于100的分数")
    m = int(input("分子m = "))  # 分子
    n = int(input("分母n = "))  # 分母
    print("输入的分数为：%d/%d" %(m, n))
    print("%d/%d 的准确值是：0." %(m, n), end="")
    for i in range(1, 101):   # i商的位数
        remainder[m] = i  # m：得到的余数remainder[m]:该余数对应的商的位数
        m *= 10  # 余数扩大10倍
        quotient[i] = m // n  # 商
        m = m % n   # 求余数
        if m == 0:   # 余数为0则表示是有限小数
            j = 1
            while j <= i:
                print("%d" %quotient[j], end="")  # 输出商
                j += 1
            break  # 退出循环

        if remainder[m] != 0:  # 若该余数对应的位在前面已经出现过
            j = 1
            while j <= i:
                print("%d" %quotient[j], end="")   # 输出循环小数
                j += 1
            print("\n分数的第一个循环节：%d" %remainder[m])
            print("循环节的起始位置为：%d" %i)
            break
