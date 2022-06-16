import os
import threading
import time
import paramiko

#定义多线程
threads = [10]

#ip地址池
ips = {
'Device1': '10.31.1.2',
'Device2': '10.31.1.3',
}
#拿到cmd.txt文件中的命令
with open('/root/baisheng_config/config_file', 'r') as f:
    cmd_line= f.readlines()
cmd=[]
for c in cmd_line:
     cmd.append(c)
#定义连接与操作
def ssh2(ips,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,ssh_port,username,passwd,timeout=5)
        ssh_shell = ssh.invoke_shell()
        for m in cmd:
            res = ssh_shell.sendall(m)
            time.sleep(float(0.4))
        print ssh_shell.recv(204800)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)

if __name__=='__main__':
    print "Begin......"
    for key in ips:
        ip = ips[key]
        a = threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        a.start() 
