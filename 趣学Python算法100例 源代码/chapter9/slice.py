#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/1 23:28 
# @desc: 序列分片


if __name__ == "__main__":
    str = "abcdefghijklmnopqrstuvwxyz" # 定义字符串

    print(str[4])  # 取字符串中序号为4的字符，也就是第5个字符串
    print(str[-3])  # 从字符串的尾部开始计算，取字符串的倒数第3个字符
    print(str[-0])  # -0即是0，也就是取字符串的第一个字符
    print(str[-1])  # 取字符串的倒数第一个字符，也就是最后一个字符

    #分片
    print(str[2:8])  # 取字符串中从第3个字符到第9个字符的内容，不包含第9个字符
    print(str[1:1])  # 不包含第2个字符，这里为空
    print(str[1:-1]) # 从第2个字符开始到最后一个字符，不包含最后一个字符
    print(str[0:-1]) # 从第1个字符到倒数第1个字符，不包含最后一个字符
    print(str[-8:-2]) # 从倒数第9个到倒数第2个字符，不包含倒数第9个字符
    print(str[-8:0]) # 打印为空，在分片中最左边的索引比它右边的索引晚出现在序列中，结果就是一个空值
    print(str[:10])  # 从第1个字符取到第11个字符，不包含第11个字符
    print(str[12:])  # 从第13个字符取到最后一个字符
    print(str[-9:])  # 从倒数第9个字符开始取
    print(str[:-4])  # 从第1个字符取到倒数第4个字符，不包含倒数第4个
    print(str[:])  #取出整个字符串
