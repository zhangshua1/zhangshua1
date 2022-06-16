import pexpect

try:

    for host in open('HK5700IPs.txt','r').readlines():
        print(host)
        #switchIP = host.strip('\\n')
        switchIP = host
        telnet = 'telnet ' + switchIP
        switchPassword = "password"
        switchEnable = 'screen-length 0 temporary'
        commandTorun = 'display current-configuration interface'
#Login to the switch
        t = pexpect.spawn(telnet)
        t.expect('Password:')
        # t.sendline('sup')
        # t.expect('word:')
        t.sendline(switchPassword)
        t.expect('>')
        t.sendline(switchEnable)
        t.expect('>')

    #Send the command
        t.sendline(commandTorun)
        t.expect('return')
        data =  t.before.decode('utf-8')   #最重要的一点，不能直接转为str必须用转码的方式

    #Closing the Telnet Connection
        t.sendline('quit')
    #t.expect('>')
    #t.sendline('quit')
        t.expect(pexpect.EOF)

    #Opening the file and writing the data to it
        f = open('Temp.txt','w')
        f.write(data)
        f.close()
        new_configure = open(switchIP.strip('\n') + '_config.txt', 'w')
        f2 = open('Temp.txt','r')
#       f.close()

        lines = f2.readlines()
        for line in lines:    #读每一行的配置
            if "#" in line:
                new_configure.write(line)
            elif "interface GigabitEthernet" in line:   #找寻端口配置命令，并生成配置命令
                new_configure.write(line)
            elif "traffic-policy P5M inbound" in line:  #找寻对应的端口下是否有限速的配置命令，并生成配置命令
                new_configure.write(" undo traffic-policy inbound\n traffic-policy P5Mnew inbound\n ")
            elif "traffic-policy P10M inbound" in line:  #找寻对应的端口下是否有限速的配置命令，并生成配置命令
                new_configure.write(" undo traffic-policy inbound\n traffic-policy P10Mnew inbound\n ")

        f.close()
        new_configure.close()
        print(host+"finish")

except Exception as e:
    print ("The Script failed to login")
    print (str(e))