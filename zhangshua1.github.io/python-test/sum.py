# 计算阶乘
# def get_jiecheng(number):
#     result = 1
#     while number > 0:
#         result *= number
#         number -= 1
#     return result
# print("jiecheng 6 = ", get_jiecheng(6))
# print("jiecheng 1000 = ", get_jiecheng(1000))

# 计算圆的面积
# import math
# print(math.pi)

# def s(r):
#     mj = round(math.pi * (r ** 2),2)
#     return mj

# print("半径为r的圆面积为：", s(3.14))

# 计算前N个数的平方和

# from unittest import result
# def sum(n):
#     result = 0
#     for number in range(0,n+1):
#         result += number * number
#     return result
# print("5以内的平方和是:",sum(5))

# 计算列表数字和

# def sum_of_list(parm_list):
#     total = 0
#     for iteam in parm_list:
#         total += iteam
#     return total
# list1 = [1,2,3,4,5]
# print(f"sum of {list1}, ", sum(list1))

# 计算数字范围内的偶数

# def szos(begin,end):
#     result = []
#     for number in range(begin,end):
#         if number % 2 == 0:
#             result.append(number)
#     return result

# begin = 4
# end = 15
# print(szos(begin,end))

# 查看目录下文件大小

from genericpath import getsize
import os

for file in os.listdir("."):
    if os.path.isfile(file) and file.endswith(".xls"):
        print(f"{file}:",  os.path.getsize(file)/1000,"kb")
print("git commit")













