import paramiko
import string
import re
#coding:utf-8
# t=paramiko.Transport((ip,port))    #设置ssh连接的远程主机地址和端口
# t.connect(username=username,password=password)      #设置登录名和密码
# chan=t.open_session()       #连接成功后打开一个channel
# chan.settimeout(session_timeout)         #设置会话超时时间
# chan.get_pty()      #打开远程的terminal
# chan.invoke_shell()       #激活terminal
# chan.send('command')      #执行远程命令
# chan.recv(recv_buffer)     #获取反馈


# #创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='10.60.100.4', port=22, username='longtian', password='LongTian!@#123')

# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('display version')
# # 获取命令结果
# result = stdout.read()
# print (str(result,encoding='utf-8'))
# # 关闭连接
# ssh.close()

def sshs():
    try:
        transport = paramiko.Transport(('10.60.100.4', 22))
        transport.connect(username='longtian', password='LongTian!@#123')

        ssh = paramiko.SSHClient()
        ssh._transport = transport

        stdin, stdout, stderr = ssh.exec_command('display version')
        version = str(stdout.read(),encoding='utf-8')
        print(version)
        ve = re.findall(r'',version)
        print(ve)
        transport.close()
    except Exception as err:
        print(err)

sshs()
# with open(r'zs.txt','wb') as f:
#     f.write(sshs().decode())
# for line in result:
#     f.writelines(line[0]) #提取指定内容，注意数据集不能有空行
#     f.writelines('\n') #换行显示





# #coding:utf-8
# import paramiko
# import uuid

# class SSHConnection(object):

#     def __init__(self, host='10.60.100.4', port=22, username='longtian',pwd='LongTian!@#123'):
#         self.host = host
#         self.port = port
#         self.username = username
#         self.pwd = pwd
#         self.__k = None

#     def connect(self):
#         transport = paramiko.Transport((self.host,self.port))
#         transport.connect(username=self.username,password=self.pwd)
#         self.__transport = transport

#     def close(self):
#         self.__transport.close()

#     # def upload(self,local_path,target_path):
#     #     # 连接，上传
#     #     # file_name = self.create_file()
#     #     sftp = paramiko.SFTPClient.from_transport(self.__transport)
#     #     # 将location.py 上传至服务器 /tmp/test.py
#     #     sftp.put(local_path, target_path)

#     # def download(self,remote_path,local_path):
#     #     sftp = paramiko.SFTPClient.from_transport(self.__transport)
#     #     sftp.get(remote_path,local_path)

#     def cmd(self, command):
#         ssh = paramiko.SSHClient()
#         ssh._transport = self.__transport
#         # 执行命令
#         stdin, stdout, stderr = ssh.exec_command(command)
#         # 获取命令结果
#         result = stdout.read()
#         v1 = str(result,encoding='utf-8')
#         with open("./vv.txt","w") as f:
#             f.write(v1.decode(ascii))
#             print(f.read())
        
#         return result
# ssh = SSHConnection()
# ssh.connect()
# ssh.cmd("ls")
# # ssh.upload('s1.py','/tmp/ks77.py')
# # ssh.download('/tmp/test.py','kkkk',)
# #ssh.cmd("df")
# ssh.close()