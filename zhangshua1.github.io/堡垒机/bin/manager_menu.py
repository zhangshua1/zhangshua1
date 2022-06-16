#!/usr/bin/python3.6
import os,sys,io
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.stdout = io.TextIOWrapper(sys.stderr.buffer,encoding='utf-8')

from modules.managr_handle import *

choices = {
    "1": "添加用户名",
    "2": "授权用户名访问主机",
    "3": "添加主机",
    "4": "删除主机",
    "5": "查看日志",
    "6": "退出"
}

while True:
    print("菜单：")
    for k, v in choices.items():
        print(k + ". " + v)
    
    choice = input("请输入编号：")
    choice = str(choices).strip()
    if choice in choices.keys():
        if choice == "1":
            add_user()
        elif choice == "2":
            authorized()
        elif choice == "3":
            add_host()
        elif choice == "4":
            del_host()
        elif choice == "5":
            view_log()
        elif choice == "6":
            quit()

    else:
        print("编号错误，请重新输入！")
        continue
