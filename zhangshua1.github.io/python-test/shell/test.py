#-*- coding: utf-8 -*-
#!/usr/bin/python 
# import paramiko
# import time
# import os
# import sys
# from conf import *
# cmd=sys.argv[1]
# swtype=sys.argv[2]
# ip = '10.60.100.4'
# user = 'longtian'
# pas = 'LonTian!@#123'
# #定义连接与操作
# def ssh2(ip,user,pas,cmd):
#         transport = paramiko.Transport((ip, 22))
#         transport.connect(username=user, password=pas)
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh._transport = transport
#         stdin, stdout, stderr = ssh.exec_command(display version)
#         result = stdout.read()
#         print(result.decode(encoding="utf-8"))
#         time.sleep(float(1))
#         transport.close()
# #判断要在哪个类型交换机上执行命令
# def swtypes(swtype):
#         if swtype=='asw' :
#             swips = aswip
#         elif  swtype=='dsw' :
#             swips = dswip
#         elif  swtype=='lsw' :
#             swips = lswip
#         elif  swtype=='isw' :
#             swips = iswip
#         elif  swtype=='cdlisw':
#             swips = cdliswip
#         elif  swtype=='omr' :
#             swips = omrip
#         elif  swtype=='csw' : 
#             swips = cswip
#         elif  swtype=='alsw' :
#             swips = alswip
#         elif  swtype=='oasw' :
#             swips = oaswip
#         else :
#             print "The swtypes error,input correct swtyps!"
#             exit()

#         for key in swips :
#             ip=swips[key]
#             ssh2(ip,user,pas,cmd)


# if __name__=='__main__':
#         print "Begin......"
#         swtypes(swtype)


# with open() as f:


import paramiko,time
def ssh():
    try:
        t = paramiko.Transport(('10.60.100.4',22))
        t.connect(username='longtian',password='LongTian!@#123')
        chan=t.open_session()
        chan.settimeout(15)
        chan.get_pty()
        chan.invoke_shell()
        chan.send("display version\n")
        # chan.send(" "*60)
        time.sleep(2)
        with open("./t.txt","w+") as f:
            f.write(chan.recv(65535).decode('ascii'))
            print(f.read())
    except Exception as err:
        print('异常信息：',err)
    finally:
        f.close()
        t.close()
ssh()