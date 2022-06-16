#!/usr/bin/env python3
#_*_coding:utf-8_*_
host = '192.168.107.156'
port = 3307
user = 'root'
passwd = '123456'
db = 'shuai'
#打开数据库连接
def exp():
	import pymysql
	
	conn = pymysql.connect(host,port,user,passwd,db,charset='utf8')

	#使用cursor()方法创建一个游标对象cursor
	cursor = conn.cursor()
	path = r"D:/Git/zhangshua1.github.io/python-test/test000/zs.txt"
	sql = "select * from addess"
	try:
		#使用execute()方法执行sql查询
		cursor.execute(sql)
		#使用fetchone()方法获取数据
		data = cursor.fetchall()
		with open(path,"a+") as f:
			f.write(data)
			# f.close()
		print(data)
		for i in data:
			id = i[0]
			name = i[1]
			sex = i[2]
			address = i[3]
			print("id=%s,name=%s,sex=%s,address=%s" % (id,name,sex,address))
	except:
	 	print("Error: unable to fetch data")

	#关闭数据库连接
	conn.close()
if __name__ == "__main__":
	exp()