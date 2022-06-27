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

# from genericpath import getsize
# import os

# for file in os.listdir("."):
#     if os.path.isfile(file) and file.endswith(".py"):
#         print(f"{file}:",  os.path.getsize(file)/1000,"kb")
#print("git commit")

# rabit=3
# print("兔子初始数量为3")

# print("请输入N：")
# ny=int(input())
# for i in range(0,ny):
#     rabit = rabit * 2
# print("%d年后，兔子数量为:%d" %(ny,rabit))

# print("请输入N:")
# N=int(input())
# sum = 0
# j = 0
# for i in range(0,N):
#     j = i + 1
#     #sum=sum*j
#     sum=sum+j
# print("sum=%d" %(sum))

# num1 = int(input("输入班级1的学生数量："))
# class1 = set()
# for i in range(0,num1):
#     name = input("输入学生%d的姓名" %(i+1))
#     class1.add(name)
# num2 = int(input("输入班级2的学生数量："))
# class2 = set()
# for i in range(0,num2):
#     name = input("输入学生%d的姓名" %(i+1))
#     class2.add(name)
# print("1班没有2班有的名字为：%s" %(class2-class1))

# xiaoming={"语文":85,"数学":96,"英语":88}
# xiaohong={"语文":72,"数学":80,"英语":91}
# xiaoliang={"语文":83,"数学":69,"英语":75}
# sum_xm = 0
# sum_xh = 0
# sum_xl = 0
# for i in xiaoming.keys():
#     sum_xm += xiaoming[i]
# for i in xiaohong.keys():
#     sum_xh += xiaohong[i]
# for i in xiaoming.keys():
#     sum_xl += xiaoliang[i]
# print("xiaoming的总成绩为:%d" %(sum_xm))
# print("xiaohong的总成绩为:%d" %(sum_xh))
# print("xiaoliang的总成绩为:%d" %(sum_xl))
# # if sum_xm > sum_xh:
#     print(sum_xm)
# elif sum_xh > sum_xl:
#     print(sum_xh)
# else:
#     print(sum_xl)
# sum=list()
# sum.append(sum_xh)
# sum.append(sum_xl)
# sum.append(sum_xm)
# print(max(sum))

# a = [['1']*3 for i in range(3)]
# print(a)

# b = [['1']]*3
# print(b)

# c=[]
# for i in range(3):
#     lis = ['1']*3
#     c.append(lis)
# print(c)

a = [1,2,3]
b = [4,5,6]
print(a+b)



















