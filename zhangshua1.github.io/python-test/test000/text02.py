import pymysql

def main():
    conn = pymysql.connect(host='192.168.107.156',
                            port=3307,
                            user='root',
                            password='123456',
                            db='shuai',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor #字典型的游标)
    try:
        with conn.cursor() as cursor:
            sql = 'select * from addess'
            cursor.execute(sql)
            a = cursor.fetchall()
            # print(a)
            for i in a:
                print(i['name'],end='\t')
                print(i['sex'],end='\t')
                print(i['add'],end='\t')
                print(i['id'])
            #     print(f'名字：{i[0]}')
            #     print(f'性别：{i[1]}')
            #     print(f'地址：{i[2]}')
            #     print(f'编号：{i[3]}')
            #     print('-' * 20)
    except pymysql.MySQLError as error:
        print(error)
    finally:
        conn.close()

if __name__ == "__main__":
    main()