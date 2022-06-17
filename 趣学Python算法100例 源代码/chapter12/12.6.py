#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : liuhefei
# @Time : 2019/8/14 22:21
# @desc: 求出符合要求的素数

# 判断素数
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  # n不是素数
    return True  # n是素数

# 求出紧靠n的k个素数
def num(n, k, array):
    i, n = 0, n + 1
    while k > 0:
        if isPrime(n):  # 调用函数isPrime判断n是否是素数
            array[i] = n  # 若n是素数，则将n存入数组array中
            i += 1
            k -= 1
        n += 1


# 文件操作
def filedata():
    array = [0] * 1000
    rf = open('infile.txt', 'r')  # 读infile.txt文件
    wf = open('outfile.txt', 'w')  # 写outfile.txt文件
    # 从infile.txt文件中读取10对(n,k)值
    for i in range(10):
        [n, k] = rf.readline().split()
        n = int(n)
        k = int(k)
        num(n, k, array)  # 调用num函数
        for n in range(k):
            print('%d ' % array[n], file=wf, end='')  # 写文件
        print(file=wf)

    rf.close()  # 关闭infile.txt文件
    wf.close()  # 关闭outfile.txt文件


if __name__ == '__main__':
    array = [0] * 1000
    print('输入整数n和k：')
    n, k = map(int, input().split())
    num(n, k, array)  # 调用num函数
    for n in range(k):
        print(array[n], end=' ')  # 打印出array数组中的每个值
    print('\n')
    filedata()  # 调用filedata函数
