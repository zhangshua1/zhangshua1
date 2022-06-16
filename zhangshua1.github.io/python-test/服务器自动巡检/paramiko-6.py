#!/usr/bin/python3.6
#使用 pexpect 模块自动登录并列出当前
import pexpect
child = pexpect.spawn('ftp 127.0.0.1')
child.expect('Name .*: ')
child.sendline('anonymous')
child.expect('Password:')
child.sendline('')
child.expect('ftp> ')
child.sendline('ls')
child.expect('ftp> ')
child.sendline('bye')
result = child.before()
for i in result.decode('utf8').split("\r\n"):
    print(i)
    
