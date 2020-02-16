import pymysql

#创建连接对象
conn=pymysql.connect(
	host='192.168.107.120',
	user='root',
	password='123456',
	database='zhang',
	charset='utf8'
	)
#从conn得到cursor对象
cursor=conn.cursor()
#执行SQL语句
sql="select * from shuai"cursor.execute(sql)
#获取结果
datas=cursor.fetchall()
#for循环输出
for data in datas:
	print(data)
#释放cursor
cursor.close()
#释放连接
conn.close()
