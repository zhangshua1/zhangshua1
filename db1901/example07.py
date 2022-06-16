import redis

client = redis.Redis(host='120.77.222.217',
                     port=6379,
                     password='1qaz2wsx')
client.ping()
client.set('username', 'wangdachui', ex=120)
print(client.get('username').decode())
print(client.ttl('username'))
client.expire('username', 300)
client.hmset('stu:1001', {'name': '王大锤', 'age': 18})
for value in client.hvals('stu:1001'):
    print(value.decode())
client.rpush('list1', 10, 20, 30, 40, 50, 60)
for value in client.lrange('list1', 0, -1):
    print(value.decode(), end=' ')
print()
# client.flushall()
