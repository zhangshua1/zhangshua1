#coding=utf-8
import pymysql
import xlwt
import importlib,sys
importlib.reload(sys)

# __Desc__ = 从数据库中导出数据到excel数据表中

def export(host,port,user,password,dbname,table_name,outputpath):
    #conn = pymysql.connect('192.168.107.156','3307','root','123456','shuai',charset='utf8')
    conn = pymysql.connect(host,port,user,password,dbname,charset='utf8')
    cursor = conn.cursor()

    count = cursor.execute('select * from '+table_name)
    print(count)
    # 重置游标的位置
    cursor.scroll(0,mode='absolute')
    # 搜取所有结果
    results = cursor.fetchall()

    # 获取MYSQL里面的数据字段名称
    fields = cursor.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('table_'+table_name,cell_overwrite_ok=True)

    # 写上字段信息
    for field in range(0,len(fields)):
        sheet.write(0,field,fields[field][0])

    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1,len(results)+1):
        for col in range(0,len(fields)):
            sheet.write(row,col,u'%s'%results[row-1][col])

        workbook.save(outputpath)

# 结果测试
if __name__ == "__main__":
    export(host='192.168.107.156',port=3307,user='root',password='123456',dbname='shuai',table_name='addess',r'foo.xls')
    #export