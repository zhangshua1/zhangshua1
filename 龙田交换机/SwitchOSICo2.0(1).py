# Version Python：3.8
# Author Leon


import time,os
from netmiko import ConnectHandler
import xlwt,xlrd
import re
from xlutils.copy import copy


class switch(object):
    """
    1. 初始化类变量[连接信息]
    2. 连接正确返回连接对象
    3. 执行命令接收连接对象并执行命令
     4. 输出到Excel表格
    """
    # 1. 初始化变量
    def __init__(self, device_type, host, username, password):
        # 初始化连接信息[类型，主机，用户名，用户密码，以及当前数量]
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

    # 2. 连接交换机
    def __connectionDevice(self):
        try:  # 2.1 尝试连接交换机并返回连接对象
            connect = ConnectHandler(device_type=self.device_type, host=self.host, username=self.username,
                                     password=self.password)
            return connect
        except Exception:  # 2.2 如果连接失败打印连接错误信息
            return  # 2.3 连接失败直接退出此次

    # 3. 执行命令
    def __execCommon(self):
        # 3.1 拿到连接对象
        connect = self.__connectionDevice()
        # 3.2 正常拿到对象开始执行命令获取信息
        if connect:
            global  deviceName # 3.2.1 暴漏主机名后面用
            deviceName = connect.send_command('dis cu | in sysname').split()[1]
            # 3.2.2 获取数据
            rest = [['接口', 'IP', 'MAC', 'VPN-INSTANCE']]
            output = connect.send_command('dis arp | in 10GE')
            data = re.compile('.+10GE.+').findall(output)
            # 3.2.3 逐行处理数据
            for dt in data:
                try:
                    rest.append([dt.split()[4],dt.split()[0],dt.split()[1],dt.split()[5]])
                except:
                    rest.append([dt.split()[4], dt.split()[0], dt.split()[1], 'null'])
            # 3.2.4 返回数据
            return rest

    # 4. 写入Excel
    def inputExcel(self):
        # 4.1 获取数据
        # data = self.__execCommon()
        data = self.__execCommon()
        # 4.2 开始处理Excel 如果Execl已存在
        excelFile = os.path.join('./', 'Switchinfo.xls')
        sheetName = time.strftime('%Y%m%d')
        try:
            workBook = xlrd.open_workbook(excelFile)
            if sheetName in workBook.sheet_names():
                workBookSheetRows = workBook.sheet_by_name(sheetName).nrows
                newWorkBook = copy(workBook)
                newWorkBookSheet = newWorkBook.get_sheet(sheetName)
                newSheetRows = workBookSheetRows + 1
                newWorkBookSheet.write_merge(newSheetRows,newSheetRows,0,8,deviceName+'  '+time.strftime('%H:%M:%S'))
                newSheetRows += 1
                for dt1 in data:
                    newSheetCols = 1
                    for dt2 in dt1:
                        snewSheetCols = newSheetCols + 1
                        newWorkBookSheet.write_merge(newSheetRows,newSheetRows,newSheetCols,snewSheetCols,dt2)
                        newSheetCols += 2
                    newSheetRows += 1
                newWorkBook.save(excelFile)
                return
            newWorkBook = copy(workBook)
            newWorkBookSheet = newWorkBook.add_sheet(sheetName)
            newSheetRows = 0
            newWorkBookSheet.write_merge(newSheetRows,newSheetRows,0,8,deviceName+'  '+time.strftime('%H:%M:%S'))
            newSheetRows += 1
            for dt1 in data:
                newSheetCols = 1
                for dt2 in dt1:
                    snewSheetCols = newSheetCols + 1
                    newWorkBookSheet.write_merge(newSheetRows, newSheetRows, newSheetCols, snewSheetCols, dt2)
                    newSheetCols += 2
                newSheetRows += 1
            newWorkBook.save(excelFile)
        except:
            #  4.2.2 不存在直接创建
            workBook = xlwt.Workbook()
            workSheet = workBook.add_sheet(sheetName)
            workSheetRows = 0
            workSheet.write_merge(workSheetRows,workSheetRows,0, 8,deviceName+'  '+time.strftime('%H:%M:%S'))
            workSheetRows += 1
            for dt1 in data:
                workSheetCols = 1
                for dt2 in dt1:
                    sworkSHeetCols = workSheetCols + 1
                    workSheet.write_merge(workSheetRows,workSheetRows,workSheetCols,sworkSHeetCols,dt2)
                    workSheetCols += 2
                workSheetRows += 1
            workBook.save(excelFile)


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