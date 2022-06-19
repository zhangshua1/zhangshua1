#!/usr/bin/env python3
#_*_coding:utf-8_*_
'''
f = open("123.txt",'a')
count = 0
for line in f:
	if count == 9:
		print('--------我是分割线---------')
		count+=1
		continue
	print(line)
	count +=1
f.close()
'''
'''
f = open("123.txt",'r')

print(f.tell())
print(f.readline())
print(f.tell())
print(f.seek(10))
print(f.readline())
print(f.encoding)
print(f.fileno())
print(f.line_buffering)
print(f.flush())
print(f.buffer)
'''
'''
import sys,time
for i in range(50):
	sys.stdout.write("#")
	sys.stdout.flush()
	time.sleep(0.1)
'''
# import os
# f = os.system(command)
# print(f)

if __name__=="__main__":
	i=0
	k=0
	for i in range(10):
		j=0
		for j in range(10):
			if j != i:
				k = 1000 * i + 100 * i + 10 * j + j
				for temp in range(31,100):
					if temp * temp == k:
						print(k)


