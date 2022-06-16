import os
import paramiko

# ips = {
# 'Device1': '192.168.90.158'
# }
# username = 'admin'
# passwd = 'baisheng@123'

# def ssh2(ips,username,passwd):
#     try:
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(ip,ssh_port,username,passwd,timeout=5)
#         ssh_shell = ssh.invoke_shell()
#         res = ssh_shell.sendall('display current-configuration | include' +  ' ' + order + '\n')
#         exsit = ssh_shell.recv(4096)
#         print(exsit)
#         ssh.close()
#     except:
#         print('%s\tError\n'%(ip))

# if __name__=='__main__':
#     print ("Begin......")
#     for key in ips:
#         ip = ips[key]
#         a = ssh2(ips,username,passwd)

# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='192.168.90.158', port=22, username='admin', password='baisheng@123')
# stdin, stdout, stderr = client.exec_command('dis cu')
# print(stdout.read().decode('utf-8'))
# client.close()

# with open('D:/Git/baisheng.log', 'r') as f:
#     cmd_line= f.readlines()
# cmd=[]
# for c in cmd_line:
#     cmd.append(c)
#     print(c)

# f = open('test.txt','w')
# f.write('woca')
# f.close()
with open('D:/Git/baisheng.log','r') as f:
    # bz = f.readline()
    for i in f.readlines():
        print(i)
    f.close()