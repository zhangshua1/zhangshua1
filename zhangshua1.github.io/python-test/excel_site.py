import xlrd
# import os

# filepath = r'D:\\Git\\zhangshua1.github.io\\test'
# fileList = os.listdir(filepath)
# print(fileList)

xlsx = xlrd.open_workbook('D:\\Git\\zhangshua1.github.io\\test\\学生名单.xlsx')
table = xlsx.sheet_by_index(0)
nrows = table.nrows
for j in range(1,nrows):
    value = table.cell_value(j,0)
    print("第1列值为",value)

print("表格一共有",nrows,"行")

name_list = [str(table.cell_value(i,2)) for i in range(1, nrows)]
print("第3列所有值：",name_list)