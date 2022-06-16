import xlwt
import importlib,sys
importlib.reload(sys)

def sql(host,port,user,password,database):
	import pymysql	
	# 打开数据库连接
	db = pymysql.connect(
    host='192.168.107.156',
    port=3307,
    user='root',
    passwd='123456',
    database='shuai',
    charset='utf8'
	)
	# db = pymysql.connect(host,port,user,password,database)
	path = r"D:/Git/zhangshua1.github.io/python-test/test000/zs.txt"
	# 使用cursor()方法创建一个游标对象cursor
	cursor = db.cursor()
	# 使用execute()方法执行SQL查询
	cursor.execute("SELECT * from addess")
	# 使用 fetchone() 方法获取单条数据.
	data = cursor.fetchall()
	
	for i in data:
		with open(path,"ab+") as f:
			f.write(str(i).encode('utf-8'))
			f.write(str('\n').encode('utf-8'))
		print(i)
	# 关闭数据库连接
	db.close()

sql(host='192.168.107.156',port=3307,user='root',password='123456',database='shuai')

