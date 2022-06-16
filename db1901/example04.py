import pymysql


class Dept:

    def __init__(self, no, name, location):
        self.no = no
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.no}\t{self.name}\t{self.location}'


# 第一步：指定主机、端口、用户名、口令、数据库、字符集创建连接
conn = pymysql.connect(host='120.77.222.217', port=3306,
                       user='root', password='Luohao.618',
                       database='hrs', charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
try:
    # 第二步：通过连接对象的cursor方法获取游标对象
    with conn.cursor() as cursor:
        # 第三步：通过游标对象的execute方法向数据库发出SQL
        cursor.execute(
            'select dno, dname, dloc from tb_dept'
        )
        # 第四步：通过游标对象抓取数据
        for row in cursor.fetchall():
            print(row)
    # 第四步：所有操作都成功就提交
    # conn.commit()
except pymysql.MySQLError as err:
    print(err)
    # 第四步：如果出现异常就回滚（撤销）
    # conn.rollback()
finally:
    # 第五步：关闭连接释放资源
    conn.close()
