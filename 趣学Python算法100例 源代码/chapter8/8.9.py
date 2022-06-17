#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/14 23:41 
# @desc: 删除“*”号


def fun(string):
    i, j = 0, -1
    while string[i] == '*': #前半部分*截止位置
        i += 1
    while string[j] == '*': #后半部分*截止位置
        j -= 1
    return i, j

if __name__ == '__main__':
    string = input('Enter a string:\n')

    start, end = fun(string)
    new_string = string[:start] + string[start:end - 1].replace('*', '') + string[end:]
    print('The string after deleted:')
    print(new_string)

