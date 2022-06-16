import pymysql

#创建连接对象
conn = pymysql.connect(
	host='192.168.107.108',
	user='root',
	password='123456',
	database='zhang',
	charset='utf8',
	port=3307
	)
#从conn得到cursor对象
cursor=conn.cursor()
#执行SQL语句
sql="select * from shuai"
cursor.execute(sql)
#获取结果
datas=cursor.fetchall()
#for循环输出
for data in datas:
	print(f'名字：{data[0]}')
	print(f'性别：{data[1]}')
	print(f'地址：{data[2]}')
	print(f'编号：{data[3]}')
	print('-' * 20)
#释放cursor
cursor.close()
#释放连接
conn.close()
