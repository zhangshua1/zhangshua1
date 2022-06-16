# # with open(r"./ip.txt") as f:
# #     ip = f.readlines()
# #     ips=[]
# #     for i in ip:
# #         ips.append(i)
# #     print(ips[1])
# # print("1")
# # import sys
# # gpus = sys.argv[1]
# # batch_size = sys.argv[2]
# # print(gpus)
# # print(batch_size)
# import re
# # data1 = [
# #     '接口', 'MAC', 'IP', 'VPN-INSTANCE', 
# #     '10GE0/0/5', 'a849-4db9-38c0', '10.60.100.250','Public_vRouter_1001', 
# #     '10GE0/0/7', 'a849-4db9-4a00', '10.60.100.180','Public_vRouter_1002', 
# #     '10GE0/0/10', 'a849-4db9-2ba0', '10.60.100.156','Public_vRouter_1003', 
# #     '10GE0/0/1', 'a849-4db9-5240', '10.60.100.170','Public_vRouter_1004', 
# #     '10GE0/0/6', '002e-c788-3a00', '10.60.100.212','Public_vRouter_1005', 
# #     '10GE0/0/8', 'a849-4db9-4c00', '10.60.100.244','Public_vRouter_1006', 
# #     '10GE0/0/9', 'a849-4db8-80c0', '10.60.100.225','Public_vRouter_1007', 
# #     '10GE0/0/11', 'a849-4db8-d0a0', '10.60.100.226','Public_vRouter_1008', 
# #     '10GE0/0/4', 'a849-4db8-8780', '10.60.100.191','Public_vRouter_1009', 
# #     '10GE0/0/3', 'a849-4db9-37c0', '10.60.100.164','Public_vRouter_1010', 
# #     '10GE0/0/2', 'a849-4db9-2740', '10.60.100.153','Public_vRouter_1011'
# # ]

# data=['GE0/0/1 vRouter_10000',
#     'GE0/0/2 vRouter_10001',
#     'GE0/0/3',
#     ]

# for i in data:
#     ss = i.split(" ")
#     for j in ss:
#         if len(ss)<=1:
#             ss.append('null')
#         print(j)

import re
from typing import Pattern
from netmiko import ConnectHandler
import xlrd,xlwt
from xlrd import sheet
from xlutils.copy import copy

# class switch(object):
#     """
#     1. 初始化类变量[连接信息]
#     2. 连接正确返回连接对象
#     3. 执行命令接收连接对象并执行命令
#     4. 输出到Excel表格
#     """
#     # 初始化变量
#     def __init__(self, device_type, host, username, password):
#         # 初始化连接信息[类型，主机，用户名，用户密码，以及当前数量]
#         self.device_type = device_type
#         self.host = host
#         self.username = username
#         self.password = password

#     # 1.连接交换机
#     def __connDev(self):
#         try:   # 1.1 尝试连接交换机并返回连接对象
#             connect = ConnectHandler(device_type=self.device_type,host=self.host,username=self.username,password=self.password)
#             return connect
#         except Exception:  # 1.2 如果连接失败打印连接错误信息
#             return    # 1.3 连接失败直接退出此次
#     def __execCommon(self):
#         # 2.1 拿到连接对象
#         connect = self.__connDev()
#         # 2.2 如果正常则开始获取信息
#         if connect:
#             global devname # 2.3 获取主机名，并全局变量主机名
#             devname = connect.send_command('dis cu | in sysname')
#             # 2.2.1 获取数据
#             output = connect.send_command('dis arp | in 10GE')
#             # 2.2.2 正则处理获取到的数据
#             interface = re.compile(r"10GE\S*").findall(output)
#             macaddress = re.compile(r"\w\w\w\w-\w\w\w\w-\w\w\w\w").findall(output)
#             ipaddress = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b").findall(output)
#             vpninstance = re.compile(r"\S*vRouter\S*").findall(output)
#             # 2.2.3 整理数据格式 固定数据头[[数据头][ins1][ins2]]
#             rest = [['接口', 'MAC', 'IP', 'VPN-INSTANCE']]

#             return rest


# data = [['接口', 'MAC', 'IP', 'VPN-INSTANCE'], ['GE0/0/5', 'a849-4db9-38c0', '10.60.100.250',],
#             ['GE0/0/7', 'a849-4db9-4a00', '10.60.100.180', 'vRouter_Prod_00003'], ['GE0/0/10', 'a849-4db9-2ba0', '10.60.100.156', 'vRouter_Prod_00004'],
#             ['GE0/0/1', 'a849-4db9-5240', '10.60.100.170', 'vRouter_Prod_00005'], ['GE0/0/6', '002e-c788-3a00', '10.60.100.212', 'vRouter_Prod_00006'],
#             ['GE0/0/8', 'a849-4db9-4c00', '10.60.100.244'], ['GE0/0/9', 'a849-4db8-80c0', '10.60.100.225'],
#             ['GE0/0/11', 'a849-4db8-d0a0', '10.60.100.226'], ['GE0/0/4', 'a849-4db8-8780', '10.60.100.191', 'vRouter_Prod_00002'],
#             ['GE0/0/3', 'a849-4db9-37c0', '10.60.100.164'], ['GE0/0/2', 'a849-4db9-2740', '10.60.100.153']]
# # abs=[]
# # vpn = u"(*.vRouter.*)"
# # Patten = re.compile(vpn)
# # results = Patten.findall(data)
# # for result in results:
# #     abs.append(result)
# for i in data:
#     # if i[3].index:
#     print(i)

# list = set(abs)
# for i in list:
#     print(i)
#interface = re.compile(r"10GE\S*").findall(data)


# def inputExcel(self):
#     # 3.1 如果excel存在则追加
#     data = self.__execCommon()
#     excelFile = os.path.join('./','switchInfo.xls')
#     if excelFile:
#         try:
#             # 3.1.1 打开已有Excel 获取sheet 以及当前所有行
#             workBook = xlrd.open_workbook(excelFile)
#             workSheet = workBook.sheet_by_index(0)
#             sheetRowNum = workSheet.nrows
#             # 3.1.2 复制当前打开对象
#             newWorkBook = copy(workBook)
#             newWorkSheet = newWorkBook.get_sheet(0)
#             # 3.1.3 向新Excel追加写入数据
#             sheetRowNum += 1
#             newWorkSheet.write(sheetRowNum, 0, devname)
#             sheetRowNum += 1
#             for dt1 in data:
#                 column = 1
#                 for dt2 in dt1:
#                     hcolumn = column + 1
#                     newWorkSheet.write_merge(sheetRowNum, sheetRowNum, column, hcolumn, dt2)
#                     column += 2
#                 sheetRowNum += 1
#             # 3.1.4 保存追加的数据
#             newWorkBook.save('switchInfo.xls')
#         except Exception: # 3.2  第一次打开则创建
#             # 3.2.1 新建Excel文件以及sheet Valid
#             snewExcel = xlwt.Workbook()
#             snewSheet = snewExcel.add_sheet('Switch')
#             excelName = 'Switchinfo.xls'
#             # 3.2.2 写入表头
#             snewSheet.write_merge(0,0,0,5,devname)
#             sheetRow = 1
#             # 3.2.3 写入数据
#             for sdt1 in data:
#                 sheetColumn = 1
#                 for sdt2 in sdt1:
#                     shcolumn = sheetColumn + 1
#                     snewSheet.write_merge(sheetRow,sheetRow,sheetColumn,shcolumn,sdt2)
#                     sheetColumn += 2
#                     sheetRow += 1
#             # 3.2.4 保存已写入数据
#             snewExcel.save(excelFile)
import time

data = [
    ['接口', 'IP', 'MAC', 'VPN-INSTANCE'], 
    ['GE0/0/5', 'a849-4db9-38c0', '10.60.100.250'], 
    ['GE0/0/7', 'a849-4db9-4a00', '10.60.100.180'], 
    ['GE0/0/10', 'a849-4db9-2ba0', '10.60.100.156'], 
    ['GE0/0/1', 'a849-4db9-5240', '10.60.100.170'], 
    ['GE0/0/6', '002e-c788-3a00', '10.60.100.212'], 
    ['GE0/0/8', 'a849-4db9-4c00', '10.60.100.244'], 
    ['GE0/0/9', 'a849-4db8-80c0', '10.60.100.225'], 
    ['GE0/0/11', 'a849-4db8-d0a0', '10.60.100.226'], 
    ['GE0/0/4', 'a849-4db8-8780', '10.60.100.191'], 
    ['GE0/0/3', 'a849-4db9-37c0', '10.60.100.164'], 
    ['GE0/0/2', 'a849-4db9-2740', '10.60.100.153']
]

workBook = xlrd.open_workbook('./switchInfo.xls')
# date_time = time.strftime("%Y-%m-%d", time.localtime())
date_time = "woca"

newWorkBook = copy(workBook)

names = workBook.sheet_names()
# print(names.index('test'))

workSheet = workBook.sheet_by_index(0)

sheetRowNum = workSheet.nrows
# newWorkSheet = newWorkBook.add_sheet(date_time)
if date_time in names:
    sheetRowNum += 1
    newWorkSheet = newWorkBook.get_sheet(names.index(date_time))
    newWorkSheet.write(sheetRowNum, 0, '设备名1')
    sheetRowNum += 1
    for dt1 in data:
        column = 1
        for dt2 in dt1:
            hcolumn = column + 1
            newWorkSheet.write_merge(sheetRowNum, sheetRowNum, column, hcolumn, dt2)
            column += 2
        sheetRowNum += 1
else:
    newWorkSheet11 = newWorkBook.add_sheet(date_time)
    newWorkBook.save('switchInfo.xls')
    print(names.index(date_time))
    sheetRowNum = 0
    newWorkSheet11 = newWorkBook.get_sheet(names.index(date_time))
    newWorkSheet11.write(sheetRowNum, 0, '设备名2')
    sheetRowNum += 1
    for dt1 in data:
        column = 1
        for dt2 in dt1:
            hcolumn = column + 1
            newWorkSheet.write_merge(sheetRowNum, sheetRowNum, column, hcolumn, dt2)
            column += 2
        sheetRowNum += 1

print(names)
print(sheetRowNum)
newWorkBook.save('switchInfo.xls')




# new_xlsc = xlsc.get_sheet(0)
# workSheet1 = xlsc.add_sheet('123')
# workSheet = excel.sheet_by_index(0)
# sheetRowNum = workSheet.nrows
# print(sheetRowNum)
# sheetRowNum+=1
# for dt in data:
#     column = 1
#     for dt2 in dt:
#         hcolumn = column +1
#         new_xlsc.write_merge(sheetRowNum, sheetRowNum, column, hcolumn, dt2)
#         column += 2
#     sheetRowNum += 1
# sheets = data.sheet_names()
# xlsc.save('./switchInfo.xls')


