#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/18 16:27 
# @desc: 文件操作


if __name__ == "__main__":
    file1 = open("test.txt", 'r', encoding='utf-8')   # 打开test.txt文件   只读
    print("test.txt的文件内容：", file1.read())

    file2 = open("test1.txt", 'w+', encoding='utf-8')  # 打开test1.txt文件中  写入
    file2.write("你好")  # 将test.txt文件内容写入test1.txt中
    file2 = open("test1.txt", 'r', encoding='utf-8')
    print("test1.txt的文件内容为：", file2.read())

    list_str = ["天国虽美","没有了你","万杯觥筹","只不过是提醒寂寞罢了"]
    file3 = open("test2.txt", 'w+', encoding='utf-8')  # 打开test1.txt文件中  写入
    file3.writelines(list_str)
    file3 = open("test2.txt", 'r', encoding='utf-8')
    print("test2.txt的文件内容为：", file3.readlines())

    # 关闭文件
    file1.close()
    file2.close()
    file3.close()

