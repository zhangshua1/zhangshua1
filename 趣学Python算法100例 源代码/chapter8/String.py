#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/24 15:11 
# @desc: 字符串


if __name__ == "__main__":
    str1 = "abcd*1234*aaaa*bbb*abcd*ABCabc"
    str2 = "Hello World!"
    print(str1.capitalize())   # 将字符串的第一个字母大写
    print(str1.count('a'))  # 获得字符串中 "a" 的数目
    print(str1.find('abc'))  # 获得字符串中“abc”的起始位置
    print("str1字符串长度：" , len(str1))
    print("连接字符串：", str1.join('你好'))
    print("拼接字符串：", str1 + str2)
    print("将字符串中的全部字母转换为大写：", str1.upper())
    print("首字母大写：", str1.title())
    print("以*分割字符串：", str1.split("*"))
    print("使用'*'号重复字符串：", str2*3)
    print("替换字符串：", str1.replace('abc', 'def'))
    print(str1.startswith(str2))  #指定字符串str2是字符串str1的开头,返回True或False
    print(str1.endswith(str2))  # 指定字符串str2是字符串str1的结尾,返回True或False
    print("abc在字符串str1中出现的最后位置：",str1.rfind('abc'))
    print("去除字符串str1的首尾字符串abc: ",str1.strip('abc')) # 去除字符串str1中的首尾指定字符串str2


    print(str2.isalnum())  # 检测字符串中是否包含0-9，A~Z、a~z
    print(str2.isalpha())  # 检测字符串是否包含A~Z,a~z
    print(str2.isdigit())  # 检测字符串是否仅包含数字
    print(str2.islower())  # 检测字符串是否均为小写字母
    print(str2.isspace())  # 检测字符串中的所有字符是否均为空白字符
    print(str2.istitle())  # 检测字符串中的单词是否为首字母大写
    print(str2.isupper())  # 检测字符串是否均为大写字母
