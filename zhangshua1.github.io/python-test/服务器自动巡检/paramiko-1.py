#!/usr/bin/python3.6
import paramiko
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
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname,port,username,password,timeout=5)
        stdin, stdout, stderr = client.exec_command('ls -l')
        stdout = stdout.read()
        error = stderr.read()
        print(hostname)
        if not error:
            print(stdout)
        else:
            print(error)

        client.close()