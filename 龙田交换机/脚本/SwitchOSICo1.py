# Version Python：3.8
# Author Leon

import time,os
from netmiko import ConnectHandler
import xlwt,xlrd
import re,threading
from xlutils.copy import copy
from xlwt.BIFFRecords import SharedStringTable

# 交换机类
class switch(object):
    """
    1. 初始化类变量[连接信息]
    2. 连接正确返回连接对象
    3. 执行命令接收连接对象并执行命令
    4. 输出到Excel表格
    """
    # 初始化变量
    def __init__(self, device_type, host, username, password):
        # 初始化连接信息[类型，主机，用户名，用户密码，以及当前数量]
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

    # 1.连接交换机
    def __connDev(self):
        try:   # 1.1 尝试连接交换机并返回连接对象
            connect = ConnectHandler(device_type=self.device_type,host=self.host,username=self.username,password=self.password)
            return connect
        except Exception:  # 1.2 如果连接失败打印连接错误信息
            return    # 1.3 连接失败直接退出此次

    # 2.执行命令
    def __execCommon(self):
        # 2.1 拿到连接对象
        connect = self.__connDev()
        # 2.2 如果正常则开始获取信息
        if connect:
            global devname # 2.3 获取主机名，并全局变量主机名
            devname = connect.send_command('dis cu | in sysname')
            # 2.2.1 获取数据
            output = connect.send_command('dis arp | in GE')
            # 2.2.2 正则处理获取到的数据
            interface = re.compile(r"GE\S*").findall(output)
            macaddress = re.compile(r"\w\w\w\w-\w\w\w\w-\w\w\w\w").findall(output)
            ipaddress = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b").findall(output)
            vpninstance = re.compile(r"\S*vRouter\S*").findall(output)
            # 2.2.3 整理数据格式 固定数据头[[数据头][ins1][ins2]]
            rest = [['接口', 'MAC', 'IP', 'VPN-INSTANCE']]
            # 2.2.4 以接口为主循环填充数据
            try:
                for num in interface:
                    # 2.2.4.1 以[]形式组织单条数据
                    insnum = interface.index(num)
                    inslist = [interface[insnum],macaddress[insnum],ipaddress[insnum],vpninstance[insnum]]
                    rest.append(inslist) # 2.2.4.2 追加单条数目
            except Exception as e:
                pass
            finally:
                for num in interface:
                    # 2.2.4.1 以[]形式组织单条数据
                    insnum = interface.index(num)
                    inslist = [interface[insnum],macaddress[insnum],ipaddress[insnum],'null']
                    rest.append(inslist) # 2.2.4.2 追加单条数目
            # 2.2.5 返回数据
            return rest

    # 3. 写入Excel数据
    def inputExcel(self):
        data = self.__execCommon()
        date_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        # 3.1 如果excel存在则追加
        excelFile = os.path.join('./','switchInfo.xlsx')
        if excelFile:
            try:
                # 3.1.1 打开已有Excel 获取sheet 以及当前所有行
                workBook = xlrd.open_workbook(excelFile)
                workSheet = workBook.sheet_by_index(0)
                sheetRowNum = workSheet.nrows
                # 3.1.2 复制当前打开对象
                newWorkBook = copy(workBook)
                newWorkSheet = newWorkBook.get_sheet(0)
                # newWorkBook1 = newWorkBook.add_sheet('test')
                # 3.1.3 向新Excel追加写入数据
                sheetRowNum += 1
                newWorkSheet.write(sheetRowNum, 0, devname)
                sheetRowNum += 1
                for dt1 in data:
                    column = 1
                    for dt2 in dt1:
                        hcolumn = column + 1
                        newWorkSheet.write_merge(sheetRowNum, sheetRowNum, column, hcolumn, dt2)
                        column += 2
                    sheetRowNum += 1
                # 3.1.4 保存追加的数据
                newWorkBook.save('switchInfo.xlsx')
            except Exception: # 3.2  第一次打开则创建
                # 3.2.1 新建Excel文件以及sheet Valid
                snewExcel = xlwt.Workbook()
                snewSheet = snewExcel.add_sheet(date_time)
                excelName = 'Switchinfo.xls'
                # 3.2.2 写入表头
                snewSheet.write_merge(0,0,0,5,devname)
                sheetRow = 1
                # 3.2.3 写入数据
                for sdt1 in data:
                    sheetColumn = 1
                    for sdt2 in sdt1:
                        shcolumn = sheetColumn + 1
                        snewSheet.write_merge(sheetRow,sheetRow,sheetColumn,shcolumn,sdt2)
                        sheetColumn += 2
                    sheetRow += 1
                # 3.2.4 保存已写入数据
                snewExcel.save(excelFile)

if __name__ == "__main__":
    # 1. 初始化
    startTime = time.strftime('%Y-%m-%d-%H-%M-%S')
    connectSuccess = connectError = 0
    connectErrorList = []
    switchList = []
    # 2. 处理用户输入交换机地址
    with open('./switchlist','r+') as f:
        for index, line in enumerate(f.readlines()):
            switchList.append(line.strip())
    # 3. 开始处理交换机
    for sw in switchList:
        try:
            ins = switch('huawei', sw, 'longtian', 'LongTian!@#123')
            ins.inputExcel()
            connectSuccess += 1
        except Exception as e:
            print('交换机: {},信息获取失败：{}'.format(sw,e))
            connectError += 1
            connectErrorList.append(sw)
    endTime = time.strftime('%Y-%m-%d-%H-%M-%S')

    # 4. 打印回显
    resultMessage = '''
        开始时间：{}
        连接成功：{}
        连接失败：{}: {}
        结束时间：{}
    '''.format(startTime,connectSuccess,connectError,connectErrorList,endTime)
    print(resultMessage)
