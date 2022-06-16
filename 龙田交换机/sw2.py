import xlwt
from netmiko import ConnectHandler
import re
comm = "dis arp | in GE"
class data(object):
    def __init__(self,device_type,host,username,password):
        self.device_type=device_type
        self.host=host
        self.username=username
        self.password=password
    def denglu(self):
        hw = {
            'device_type': self.device_type, 
            'host': self.host, 
            'username': self.username, 
            'password': self.password,
        }
        conn = ConnectHandler(**hw)
        output = conn.send_command(comm)
        return output

    def wri(self):
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        title = ['主机名','IP','MAC','INTERFACE','VPN-INSTACE']
        row = 0
        for t in title:
            sheet.write(0,row,t)
            row+=1
    row = 1
    da = ['vRouter_Prod10003',
        'vRouter_Prod10004',
        'vRouter_Prod10005',
        'vRouter_Prod10005',
        'vRouter_Prod10006',
        ]
        
    for d in da:
        col = 0
        for one in d:
            sheet.write(row,col,one)
            col+=1
        row+=1
    book.save('test.xls')



if __name__ == "__main__":
    ins=data("huawei","10.60.100.16","longtian","LongTian!@#123")
    # retu = re.findall('\d{1,2}.\d{1,3}.\d{1,3}.\d{1,3}',ins.denglu())
    len5
    # pattern_ip = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
    l
    # retu = pattern_ip.findall(ins.denglu())
    3
    # for ip in retu:
    #     print('IP: %s'%ip)
    ins.wri()

