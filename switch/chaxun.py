# -*- coding: utf-8 -*-
import os
import time
import paramiko
#import xlrd


ips = {
'Device1': '10.31.1.1',
'Device2': '10.31.1.2',
'Device3': '10.31.1.3'
}


def ssh2(ips,username,passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,ssh_port,username,passwd,timeout=5)
        ssh_shell = ssh.invoke_shell()
        res = ssh_shell.sendall('display current-configuration | include' +  ' ' + order + '\n')
        exsit = ssh_shell.recv(4096)
        if ( exsit.count(order)  <= 1 ):
            print "设备 %s 目前没有该项配置" % (ip)
        else:
            print "设备 %s 目前有该项配置" % (ip)
        ssh.close()
    except:
        print '%s\tError\n'%(ip)

if __name__=='__main__':
    print "Begin......"
    for key in ips:
        ip = ips[key]
        a = ssh2(ips,username,passwd)