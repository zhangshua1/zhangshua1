from xlutils.copy import copy
import xlwt
import xlrd

data1 = [
    ['接口', 'IP', 'MAC', 'VPN-INSTANCE'], 
    ['10GE0/0/5', 'a849-4db9-38c0', '10.60.100.250','Public_vRouter_1001'], 
    ['10GE0/0/7', 'a849-4db9-4a00', '10.60.100.180','Public_vRouter_1002'], 
    ['10GE0/0/10', 'a849-4db9-2ba0', '10.60.100.156','Public_vRouter_1003'], 
    ['10GE0/0/1', 'a849-4db9-5240', '10.60.100.170','Public_vRouter_1004'], 
    ['10GE0/0/6', '002e-c788-3a00', '10.60.100.212','Public_vRouter_1005'], 
    ['10GE0/0/8', 'a849-4db9-4c00', '10.60.100.244','Public_vRouter_1006'], 
    ['10GE0/0/9', 'a849-4db8-80c0', '10.60.100.225','Public_vRouter_1007'], 
    ['10GE0/0/11', 'a849-4db8-d0a0', '10.60.100.226','Public_vRouter_1008'], 
    ['10GE0/0/4', 'a849-4db8-8780', '10.60.100.191','Public_vRouter_1009'], 
    ['10GE0/0/3', 'a849-4db9-37c0', '10.60.100.164','Public_vRouter_1010'], 
    ['10GE0/0/2', 'a849-4db9-2740', '10.60.100.153','Public_vRouter_1011']
]
class zhuijia(object):
    def __init__(self,filepath):
        self.filepath = filepath
    def file(self):
        xls = xlrd.open_workbook(self.filepath)
        sheet1 = xls.sheet_by_index(0)
        rowL = sheet1.nrows
        newFile = copy(xls)
        newSheet = newFile.get_sheet(0)
        rowL += 1
        for dt in data1:
            col = 1
            for sw in dt:
                hcol = col + 1
                newSheet.write_merge(rowL,rowL,col,hcol,sw)
                col += 2
            rowL += 1
        newFile.save(self.filepath)

        xlsc = copy(xls)
        shtc = xlsc.get_sheet(0)


if __name__ == "__main__":
    ins = zhuijia('./test.xls')
    for x in range(100):
        ins.file()