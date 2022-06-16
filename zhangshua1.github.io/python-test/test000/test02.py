import xlwt
workbook = xlwt.Workbook(encoding= 'utf-8')
worksheet = workbook.add_sheet('My_Worksheet')
worksheet.write(0,1, label = 'this is test')
workbook.save('D:/Git/zhangshua1.github.io/python-test/test000/Excel_test.xls')
