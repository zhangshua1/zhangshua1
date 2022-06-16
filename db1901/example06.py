"""
pymysql获取的数据库连接对象并不是线程安全的（在多线程环境下会出错）
如果希望每个线程都持有自己的资源避免因为资源竞争导致的加锁排队
可以使用threading模块的local类来实现将资源跟线程绑定，让每个线程持有自己的资源
可以通过setattr和getattr实现local对象绑定/获取属性从而实现将资源跟线程绑定
"""
import json
import threading
from concurrent.futures.thread import ThreadPoolExecutor

import pymysql
import requests

pool = ThreadPoolExecutor(max_workers=10)


# 1. 位置参数（*前面的参数）
# 2. 可变参数（*args）- arguments
# 3. 关键字参数（**kwargs）- keyword arguments
# 4. 命名关键字参数（*后面的参数） - 传参必须使用"参数名=参数值"的形式
def get_db_conn(*, autocommit=False):
    return pymysql.connect(host='120.77.222.217', port=3306,
                           user='root', password='123456',
                           database='hrs', charset='utf8',
                           autocommit=autocommit)


def main():
    conn = get_db_conn(autocommit=True)
    try:
        futures = []
        for page in range(1, 11):
            resp = requests.get(f'http://api.tianapi.com/topnews/?key=9aeb28ee8858a167c1755f856f830e22&page={page}&num=10')
            newslist = json.loads(resp.text)['newslist']
            with conn.cursor() as cursor:
                for news in newslist:
                    cursor.execute(
                        'insert into tb_news (title, description, url, source, ctime) values (%s, %s, %s, %s, %s)',
                        (news['title'], news['description'], news['url'], news['source'], news['ctime'])
                    )
                    futures.append(pool.submit(update_photo, cursor.lastrowid, news['picUrl']))
        pool.shutdown()
        for future in futures:
            future.result()
    finally:
        conn.close()


def update_photo(newsid, picurl):
    thread_local = threading.local()
    if not getattr(thread_local, 'connection', None):
        setattr(thread_local, 'connection', get_db_conn())
    if picurl:
        resp = requests.get(picurl)
        with thread_local.connection.cursor() as cursor:
            cursor.execute(
                'update tb_news set photo=%s where newsid=%s',
                (resp.content, newsid)
            )
        thread_local.connection.commit()


if __name__ == '__main__':
    main()
