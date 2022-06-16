#!/usr/bin/python3.6
#上传目录到远程服务器
import os, sys
import paramiko
local_path = '/root/test'
remote_path = '/opt/test'

if local_path[-1] == '/':
        local_path = local_path[0:-1]
if remote_path[-1] == '/':
        remote_path = remote_path[0:-1]
file_list = []
os.path.isdir(local_path):
   for root, dirs, files in os.walk(local_path):
        for file in files:
            file_path = os.path.join(root, file)
             file_list.append(file_path)
else:
    print(path + "目录不存在!")
    sys.exit(1)

with open("host.info") as f:
    while f:
        line = f.readline()
        if not line:
            break
        line = line.split()
        hostname = line[0]
        port = int(line[1])
        username = line[2]
        password = line[3]
        try:
            s = paramiko.Transport((hostname, port))
            s.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(s)
        except Exception as e:
            print(e)
            print(hostname)
        for local_file in file_list:
            remote_file = local_file.replace(local_path, remote_path)
            remote_dir = os.path.dirname(remote_file)
            try:
                sftp.stat(remote_dir)
            except IOError:
                sftp.mkdir(remote_dir)
            print("%s -> %s" % (local_file, remote_file))
            sftp.put(local_file, remote_file)
        s.close()
