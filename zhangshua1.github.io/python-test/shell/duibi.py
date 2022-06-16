import paramiko

hostname = '10.60.100.4'
username = 'root'
password = 'baisheng@123'
paramiko.util.log_to_file('syslogin.log')     #发送paramiko日志到syslogin.log文件


ssh = paramiko.SSHClient()          #创建一个SSH客户端client对象
ssh.load_system_host_keys()         #获取客户端host_keys,默认~/.ssh/known_hosts,非默认路径需指定ssh.load_system_host_keys(/xxx/xxx) 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=22,username=username,password=password,compress=True)    #创建SSH连接
stdin,stdout,stderr = ssh.exec_command('display current-configuation')      #调用远程执行命令方法exec_command()
print(stdout.readlines().decode('utf-8'))        #打印命令执行结果，得到Python列表形式，可以使用stdout_readlines()
ssh.close()

