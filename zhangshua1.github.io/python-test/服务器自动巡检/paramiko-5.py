#!/usr/bin/python3.6
#从远程服务器下载文件
import os, sys
import paramiko

hostname = '192.168.107.108'
port = 22
username = 'root'
password = '193256'
local_path ='/root/test.txt'
remote_path = '/opt/test.txt'
try:
    s = paramiko.Transport((hostname, port))
    s.connect(username=username, password=password)
    sftp = parmiko.SFTPClient.from_transport(s)
except Exception as e:
    print(e)
    sys.exit(1)
try:
    sftp.file(remote_path)
    sftp.get(remote_path, local_path)
except IOErrot as e:
    print(remote_path + "远程服务器文件不存在")
    sys.exit(1)
finally:
    s.close()
if os.path.isfile(local_path):
    print("下载成功")
else:
    print("下载失败！")
