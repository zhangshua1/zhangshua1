import pymysql

def main():
    no = int(input('输入要更新的表的编码：'))
    add = input('输入要更新的新地址:')
    conn = pymysql.connect(host='192.168.107.108',
                            port=3307,
                            user='root',
                            password='123456',
                            db='zhang',
                            charset='utf8')
    try:
        with conn.cursor() as cursor:
            abc = cursor.execute(
                'update shuai set add=%s where id=%s',(add,no))
            if abc == 1:
                print("执行成功！")
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()