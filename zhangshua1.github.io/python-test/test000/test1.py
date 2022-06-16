# '''for i in range(0,10):
# 	if i < 5:
# 		print("loop",i)
# '''
# '''
# for i in range(10):
# 	print("--------",i)
# 	for j in range(10):
# 		print(j)
# 		if j>5:
# 			break
# '''
# '''
# import sys
# print(sys.argv) #打印环境变量
# '''
# import os
#cmd_res = os.system("dir")#执行命令不保存结果
# cmd_res = os.popen("dir").read()
# print(cmd_res,"----->")
# os.mkdir("new_dir")
# path = os.getcwd()
# path1 = os.path.split(path)
# print(path1)
# result = os.path.split(path)
# print(result[1])
# dir = os.listdir(r, 'c:')
# print(dir)
# path = r'D:\\aa\\bb'
# print(path)
# firelist = os.listdir(path)
# for fire in firelist:
# 	path1 = os.path.join(path,fire)
# 	os.remove(path1)
# else:
# 	os.rmdir(path)
# 	print("删除成功！")

# dir = os.chdir('D:\\aa\\')
# path = os.getcwd()
# print(path)
import requests
import urllib.request
from bs4 import BeautifulSoup
res = urllib.request.urlopen('http://www.baidu.com')
# print(res.readlines())
# print(type(res))
soup = BeautifulSoup(res,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)