import os
import threading
import time
import paramiko
#import xlwt
#import xlrd

#定义多线程
threads = [10]

#ip地址池
ips = {
'Device1': '192.168.80.111'
}

#定义连接与操作
def ssh2(ips,username,passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,ssh_port,username,passwd,timeout=5)
        ssh_shell = ssh.invoke_shell()
        res = ssh_shell.sendall('display current-configuration | include ipsec sha2 compatible enable')
        time.sleep(float(3))
        exsit = ssh_shell.recv(4096)
        print exsit
        print exsit.count(ipsec sha2 compatible enable)
        if ( exsit.count(ipsec sha2 compatible enable) <= 1 ):
            print "设备 %s 目前没有该项配置" % (ip)
        else:
            print "设备 %s 目前有该项配置" % (ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)

if __name__=='__main__':
    print "Begin......"
    for key in ips:
        ip = ips[key]
        a = threading.Thread(target=ssh2,args=(ip,username,passwd))
        a.start() 