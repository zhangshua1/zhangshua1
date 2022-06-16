#!/usr/bin/python3.6
#上传文件到远程服务器
import os
import paramiko
local_path = '/root/test.txt'
remote_path = '/opt/test.txt'
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
        if not os.path.isfile(local_path):
            print(local_path + "文件不存在！")
            sys.exit(1)
        try:
            s = paramiko.Transport((hostname,port))
            s.connect(username = username,password=password)
        except Exception as e:
            print(e)
            sys.exit(1)
        sftp = paramiko.SFTPClient.from_transport(s)
        sftp.put(local_path,remote_path)
        try:
            sftp.file(remote_path)
            print("%s 上传成功。" %hostname)
        except IOError:
            print("%s 上传失败！" %hostname)
        finally:
            s.close()
