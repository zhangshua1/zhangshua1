import xlwt
import xlrd
from xlutils.copy import copy
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

book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
row = 0
for d in data:
    col = 0
    for one in d:
        sheet.write(row,col,one)
        col+=1
    row+=1
book.save('test.xls')

xls = xlrd.open_workbook(r'D:/Git/龙田交换机/test.xls',formatting_info = True)

xlsc = copy(xls)
shtc = xlsc.get_sheet(0)
shtc.write(row,col,'追加的1')
xlsc.save('test.xls')

