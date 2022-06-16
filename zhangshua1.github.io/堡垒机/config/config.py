database='test'
ip='192.168.107.108'
port=3307
user='root'
password='123456'

engine_param = 'mysql+pymysql://%s:%s@%s:%d/%s?charset=utf8' %(user, password, ip, port, database)
