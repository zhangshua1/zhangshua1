#!/usr/bin/python3.6
#import os,sys
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)
import re
from modules.table_init import *
from modules.db_conn import session

def add_user():
    username = input("请输入要添加的用户名：").strip()
    user = User(username=username)
    session.add(user)
    session.commit()
    print("添加成功。")

def authorized():
    n = 1
    while True:
        username = input("请输入要授权的用户名: ").strip()
        user = session.query(User).filter(User.username==username).first()
        if user:
            break
        else:
            if n == 3:
                print("输入错误次数达到3次，退出！")
                return
            print("用户名不存在，请重新输入！")
            n += 1
            continue
    n = 1
    while True:
        ip = input("请输入要授权的主机IP地址：").strip()
        host = session.query(Host).filter(Host.ip==ip).first()
        if host:
            break
        else:
            if n == 3:
                print("错误次数达到3次，退出!")
                return
            print("主机IP地址不存在，请重新输入！")
            n += 1
            continue
        n = 1
    while True:
        sudo = input("需要sudo到root权限？(Y/N): ").strip()
        if sudo in ['y', 'Y', 'N']:
            break
        else:
            if n == 3:
                print("错误次数达到3次，退出！")
                return
            print("输入错误，请重新输入！")
            n += 1
            continue

    hosts = eval(user.hosts)
    if sudo in ['y', 'Y']:
        hosts['sudo'].append(ip)
    elif sudo in ['n', 'N']:
        hosts['no-sudo'].append(ip)
    user = session.query(User).filter(User.username==username).update({"hosts":str(hosts)})
    session.commit()
    print("添加成功。")

def add_host():
    n = 1
    while True:
        ip = input("请输入要添加的IP：").strip()
        ip_match = re.match('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', ip)
        if ip_match:
            host = Host(ip=ip)
            session.add(host)
            session.commit()
            print("添加成功。")
            break
        else:
            if n == 3:
                print("错误次数达到3次，退出！")
                break
            print("IP地址错误，请重新输入！")
            n +=1
            continue

def del_host():
    n = 1
    while True:
        ip = input("请输入要删除的IP地址：").strip()
        host = session.query(Host).filter(Host.ip==ip).first()
        if host:
            session.delete(host)
            session.commit()
            print("删除成功。")
            break
        else:
            if n == 3:
                print("错误次数达到3次，退出！")
                break
            print("IP地址不存在，请重新输入！")
            n +=1
            continue

def view_log():
    logs = session.query(Cmd_log).all()
    if logs:
        for i in logs:
            print("login_user: %s | share_user: %s | server_ip: %s | shell_command: %s | datetime: %s" %(i.login_user, i.share_user, i.server_ip, i.shell_command, i.datetime))
    else:
        print("没有日志记录。")

def quit():
    sys.exit()
    