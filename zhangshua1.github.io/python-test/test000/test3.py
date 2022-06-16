import pymysql
import csv
 
def from_mysql_get_all_info():
    conn = pymysql.connect(
        host='192.168.107.156',
        port=3307,
        user='root',
        db='shuai',
        password='123456',
        charset='utf8mb4')
    cursor = conn.cursor()
    sql = 'select * from addess'
    cursor.execute(sql.encode('utf-8'))
    data = cursor.fetchall()
    conn.close()
    return data
 
 
def write_csv():
    data = from_mysql_get_all_info()
    filename = 'D:/Git/zhangshua1.github.io/python-test/test000/corpus.csv'#文件名和路径
    with open(filename,mode='w',encoding='utf-8') as f:
        write = csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)
 
write_csv()