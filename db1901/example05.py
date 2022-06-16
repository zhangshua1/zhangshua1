"""
create table tb_photo
(
photoid integer auto_increment,
url varchar(1024) not null,
imagedata longblob,
primary key (photoid)
);
"""
import pymysql
import requests

url = 'https://www.baidu.com/img/dong1_a1c52951c1f40e1496b46b9ae415c121.gif'
resp = requests.get(url)
# 第一步：指定主机、端口、用户名、口令、数据库、字符集创建连接
conn = pymysql.connect(host='120.77.222.217', port=3306,
                       user='root', password='123456',
                       database='hrs', charset='utf8',
                       autocommit=True)
try:
    # 第二步：通过连接对象的cursor方法获取游标对象
    with conn.cursor() as cursor:
        # 第三步：通过游标对象的execute方法向数据库发出SQL
        result = cursor.execute(
            'insert into tb_photo (url, imagedata) values (%s, %s)',
            (url, resp.content)
        )
        if result == 1:
            print('新增部门成功!!!')
    # 第四步：所有操作都成功就提交
    # conn.commit()
except pymysql.MySQLError as err:
    print(err)
    # 第四步：如果出现异常就回滚（撤销）
    # conn.rollback()
finally:
    # 第五步：关闭连接释放资源
    conn.close()
