#!/usr/bin/python3.6
import os,sys,io
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

from modules.table_init import *
from modules.db_conn import session
from modules.ssh_login import ssh_login
import getpass

login_user = getpass.getuser()
server_port = 22
share_user = {'sudo': 'admin', 'no-sudo': 'user', 'password': '123456'}

user_host = session.query(User).filter(User.username==login_user).first()

if login_user == "root":
    sys.exit()
if not user_host:
    print("数据库未记录该登录用户，请联系管理员！")
    sys.exit()
sudo = set(eval(user_host.hosts)['sudo'])
no_sudo = set(eval(user_host.hosts)['no-sudo'])

def display_menu():
    print("主机列表：")
    if not sudo and not no_sudo:
        print("没有授权的主机！")
    for i in sudo:
        print(i + " sudo")
    for i in no_sudo:
        print(i)

n = 1
while True:
    display_menu()
    server_ip = input(str("请输入要登陆的主机IP地址："))
    if server_ip in sudo:
        ssh_login(login_user,share_user['sudo'],server_ip,server_port,share_user['password'])
    elif server_ip in no_sudo:
        ssh_login(login_user,share_user['no-sudo'],server_ip,server_port,share_user['password'])
    else:
        if n == 3:
            print("错误次数达到3次，退出！")
            os.system("exit")
        print("IP地址错误，请重新输入！")
        n += 1
        continue
    