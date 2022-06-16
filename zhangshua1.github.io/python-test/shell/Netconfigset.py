#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# version 0.01


import socket, os, time, re
import paramiko
import commands


class Connection(object):

    # 定义ssh连接
    @staticmethod
    def ssh():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return ssh


class Device(object):

    # 初始化参数
    def __init__(self, hostname, ip, user, passwd):
        self.hostname = hostname
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.port = 22
        self.get_config_flag = True
        self.success_count = 0
        self.fail_count = 0
        self.ssh = Connection().ssh()

    # 登录设备
    def login(self):
        try:
            self.ssh.connect(self.ip, self.port, self.user, self.passwd, look_for_keys=False, timeout=10)
        except paramiko.ssh_exception.AuthenticationException as e:
            self.get_config_flag = False
            print('%s - %s - %s' % (self.hostname, self.ip, e))
        except socket.timeout as e:
            self.get_config_flag = False
            print('%s - %s - %s' % (self.hostname, self.ip, e))
        else:
            print('%s - %s - login successful' % (self.hostname, self.ip), end='')

    def run_cmds(self):
        pass


class Junos(Device):

    def __init__(self, hostname, ip, user, passwd):
        super().__init__(hostname, ip, user, passwd)
        self.junos_cmds = commands.Junos

    # 执行设备命令
    def run_cmds(self):
        if self.get_config_flag:
            vty = self.ssh.invoke_shell()
            for c in self.junos_cmds:
                time.sleep(0.1)
                vty.send('%s\n' % c)
            time.sleep(5)
            config = vty.recv(65535).decode('ascii')
            self.ssh.close()
            config_error_flag = re.findall(r'syntax error|ambiguous|unknown command', config)
            if config_error_flag:
                print('config error: %s' % config_error_flag[0])
                self.fail_count = 1
            elif config.endswith('> '):
                FileOps().write(self.hostname, self.ip, config)
                self.success_count = 1
                print(' - config successful.')
            else:
                self.fail_count = 1
                print(' - configure occurred unknow error.')
        else:
            self.fail_count = 1


class ComwareV5(Device):

    def __init__(self, hostname, ip, user, passwd):
        super().__init__(hostname, ip, user, passwd)
        self.comwarev5_cmds = commands.ComwareV5

    # 执行设备命令
    def run_cmds(self):
        if self.get_config_flag:
            vty = self.ssh.invoke_shell()
            vty.send('screen-length disable\n')
            for c in self.comwarev5_cmds:
                time.sleep(0.1)
                vty.send('%s\n' % c)
            time.sleep(5)
            config = vty.recv(65535).decode('gbk', 'ignore')
            self.ssh.close()
            config_error_flag = re.findall(r'Unrecognized command|Wrong parameter|Ambiguous command|---- More ----',
                                           config)
            if config_error_flag:
                print('get config error: %s' % config_error_flag)
                self.fail_count = 1
            elif config.endswith('>'):
                FileOps().write(self.hostname, self.ip, config)
                self.success_count = 1
                print(' - get config successful.')
            else:
                self.fail_count = 1
                print(' - get configure occurred unknow error.')
        else:
            self.fail_count = 1


class Rgos(Device):

    def __init__(self, hostname, ip, user, passwd):
        super().__init__(hostname, ip, user, passwd)
        # 开启enable密码，默认enable密码和登录密码相同
        self.enable_passwd_flag = True
        self.rgos_cmds = commands.RGOS

    # 执行设备命令
    def get_config(self):
        if self.get_config_flag:
            vty = self.ssh.invoke_shell()
            # 输入enable密码，默认和登录密码相同
            if self.enable_passwd_flag:
                vty.send('enable\n')
                time.sleep(0.1)
                vty.send(self.passwd + '\n')
            vty.send('terminal length 0\n')
            for c in self.rgos_cmds:
                time.sleep(0.1)
                vty.send('%s\n' % c)
            time.sleep(5)
            config = vty.recv(65535).decode('gbk', 'ignore')
            self.ssh.close()
            config_error_flag = re.findall(r'Invalid input detected|Incomplete command|Ambiguous command|--More--|Unrecognized host or address',
                                           config)
            if config_error_flag:
                print('get config error: %s' % config_error_flag)
                self.fail_count = 1
            elif config.endswith('#'):
                FileOps().write(self.hostname, self.ip, config)
                self.success_count = 1
                print(' - get config successful.')
            else:
                self.fail_count = 1
                print(' - get configure occurred unknow error.')
        else:
            self.fail_count = 1


class Vrp(Device):

    def __init__(self, hostname, ip, user, passwd):
        super().__init__(hostname, ip, user, passwd)
        self.vrp_cmds = commands.VRP

    # 执行设备命令
    def get_config(self):
        if self.get_config_flag:
            vty = self.ssh.invoke_shell()
            vty.send('screen-length 0 temporary\n')
            for c in self.vrp_cmds:
                time.sleep(0.1)
                vty.send('%s\n' % c)
            time.sleep(10)
            config = vty.recv(65535).decode('utf-8', 'ignore')
            self.ssh.close()
            config_error_flag = re.findall(r'Unrecognized command|Incomplete command|---- More ----',
                                           config)
            if config_error_flag:
                print('get config error: %s' % config_error_flag)
                self.fail_count = 1
            elif config.endswith('>'):
                FileOps().write(self.hostname, self.ip, config)
                self.success_count = 1
                print(' - get config successful.')
            else:
                self.fail_count = 1
                print(' - get configure occurred unknow error.')
        else:
            self.fail_count = 1


class Ios(Device):

    def __init__(self, hostname, ip, user, passwd):
        super().__init__(hostname, ip, user, passwd)
        # 开启enable密码，默认enable密码和登录密码相同
        self.enable_passwd_flag = True
        self.ios_cmds = commands.IOS

    # 执行设备命令
    def run_cmds(self):
        if self.get_config_flag:
            vty = self.ssh.invoke_shell()
            if self.enable_passwd_flag:
                vty.send('enable\n')
                time.sleep(0.1)
                vty.send(self.passwd + '\n')
                time.sleep(0.1)
            vty.send('terminal length 0\n')
            for c in self.ios_cmds:
                time.sleep(0.1)
                vty.send('%s\n' % c)
            time.sleep(5)
            config = vty.recv(65535).decode('ascii')
            self.ssh.close()
            config_error_flag = re.findall(r'Invalid input detected|Incomplete command|--More--|Unknown command or computer name',
                                           config)
            if config_error_flag:
                print('config error: %s' % config_error_flag)
                self.fail_count = 1
            elif config.endswith('#'):
                FileOps().write(self.hostname, self.ip, config)
                self.success_count = 1
                print(' - config successful.')
            else:
                self.fail_count = 1
                print(' - configure occurred unknow error.')
        else:
            self.fail_count = 1


class DeviceFactory(object):

    # 判断设备OS类型，自动实例化
    @staticmethod
    def create(*args):
        if args[4] == 'Junos':
            return Junos(*args[0:-1])
        elif args[4] == 'ComwareV5':
            return ComwareV5(*args[0:-1])
        elif args[4] == 'RGOS':
            return Rgos(*args[0:-1])
        elif args[4] == 'VRP':
            return Vrp(*args[0:-1])
        elif args[4] == 'IOS':
            return Ios(*args[0:-1])
        else:
            raise ValueError('不支持该设备类型')


class FileOps(object):

    cfg_path = None

    # 创建配置文件保存目录
    @staticmethod
    def create_config_dir():
        date = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        FileOps.cfg_path = 'cfg_%s' % date
        os.mkdir(FileOps.cfg_path)

    # 读取设备登录文件
    @staticmethod
    def read():

        with open('device.txt', 'r', encoding='utf-8') as f:
            info = f.read().split('\n')
        for i in info:
            if i[0] == '#':
                pass
            else:
                yield i.split()

    # 接收设备执行命令返回信息,写入txt文件
    @staticmethod
    def write(hostname, ip, config):
        file = '.%s%s%s%s-%s.txt' % (os.sep, FileOps.cfg_path, os.sep, hostname, ip)
        with open(file, 'w') as f:
            f.write(config)


# 程序主入口
def main():
    print('%s NetConfigSet is running, please wait a moment.\n' % time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                           time.localtime()))
    all_success_count = 0
    all_fail_count = 0
    all_device_count = 0
    cred_info = []
    cmds = []
    start_time = time.time()
    # 创建备份目录
    FileOps().create_config_dir()
    try:
        for i in FileOps().read():
            cred_info.append(i)
    except IndexError:
        os.rmdir(FileOps().cfg_path)
        print('Check the contents of device.txt in the current directory for Spaces or formatting errors.')
        raise
    # 遍历登陆信息，执行命令
    for i in cred_info:
        device = DeviceFactory()
        r1 = device.create(*i)
        r1.login()
        r1.run_cmds()
        all_success_count += r1.success_count
        all_fail_count += r1.fail_count
        all_device_count += 1
    end_time = time.time()
    # 条件判断，如果所有设备执行命令失败，删除创建的目录
    if not all_success_count:
        os.rmdir(FileOps().cfg_path)

    print('')
    print('成功数量：%d' % all_success_count)
    print('失败数量：%d' % all_fail_count)
    print('总数量：%d' % all_device_count)
    print('总共花费时间：%ds' % (end_time - start_time))


if __name__ == "__main__":
    main()