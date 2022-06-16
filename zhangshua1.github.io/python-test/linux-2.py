from common.connectionLinux.Linux import Linux
 
class App(object):
    #主节点服务器IP地址
    MASTIP = '192.168.107.152'
    #多个服务器IP地址
    IPlist = ['192.168.107.153','192.168.107.154']
 
    def __init__(self):
        self.host = Linux(self.MASTIP, 'root', '1')
    #非root账户登录
    def connect(self):
        self.host.connect()
 
    #切换root账户登录
    def sendCmdRoot(self):
        pattern1 = r'.*(密码).*'
        pattern2 = r'.*(]#).*'
        cmd1 = 'su root'
        cmd2 = '1'
        self.host.send(cmd1,pattern1)
        self.host.send(cmd2,pattern2)
 
    #子节点文件拷贝到主节点
    def copyCmd(self):
        for ip in self.IPlist:
            print(ip)
 
        pattern = r'.*(]#).*'
        cmd = 'scp root@'+ip+':/home/long/test.txt /home/long'
        print(cmd)
        self.host.send(cmd,pattern)
 
if __name__ == '__main__':
    #连接linux
    app = App()
    # app.connect()
    # app.sendCmdRoot()
    app.copyCmd()