from netmiko import ConnectHandler
import re
from xlwt import Workbook
# import openpyxl

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

#打印设备名称
   def sname(self):
      hw2 = { 
         'device_type': 'huawei', 
         'host': '10.60.100.16', 
         'username': 'longtian', 
         'password': 'LongTian!@#123', 
         }
      conn = ConnectHandler(**hw2)
      #conn.find_prompt()
      output = conn.send_command("display current-configuration | include sysname").split()[1]
      return output



if __name__ == "__main__":
   ins=data("huawei","10.60.100.16","longtian","LongTian!@#123")
   #retu = re.findall('\d{1,2}.\d{1,3}.\d{1,3}.\d{1,3}',ins.denglu())
   # pattern_ip = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
   # retu = pattern_ip.findall(ins.denglu())
   # for ip in retu:
   #    print('IP: %s'%ip)
   # pattern_mac = re.compile(r"\w\w\w\w-\w\w\w\w-\w\w\w\w")
   # mac_list = pattern_mac.findall(ins.denglu())
   # for mac in mac_list:
   #    print('MAC: %s'%mac)
   pattern_int = re.compile(r"GE.*")
   int_list = pattern_int.findall(ins.denglu())
   for i in int_list:
      print('interface: %s'%i)
   # def fillInExcel(mac_list,mac_list,valueList1):
   #      sheetA = wb[mac_list]
   #      for i in range(len(mac_list)):
   #               sheetA['A%d' % (i + 1)] = srcList[i]
   # wb = openpyxl.Workbook()
   # wb.create_sheet("IP")
   # fillInExcel('接口流量指标', interfaceList)
   # file = 'abc.xlsx'
   # wb.save(file)
   # lastlist = []
   # findword = u"('\d{1,2}.\d{1,3}.\d{1,3}.\d{1,3}')"
   # pattern = re.compile(findword)
   # results = pattern.findall(ins.denglu())
   # for result in results:  
   #  #print result
   #    lastlist.append(result)

   # list = set(lastlist)
   # for l in list:
   #    print(l)


# wb=Workbook()
# print(wb.get_active_sheet())
# wb.create_sheet('feng',3)                  ###可以加索引，也可以不加，如下条代码。
# wb.create_sheet(title='huan',index=4)
# wb.remove('huan')
# wb.remove_sheet('feng')
# wb.get_active_sheet()
   



