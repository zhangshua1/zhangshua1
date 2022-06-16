from docx import Document
import re
import os
import docx

filepath = r'D:\\Git\\zhangshua1.github.io\\test'
fileList = os.listdir(filepath)
#print(fileList)

savepath = r'D:\\张帅\\Documents'

for docxname in fileList:
    #print(docxname)
    docxpathname = filepath + '\\' + docxname
    document = docx.Document(docxpathname)

    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            if "成佳瑶" in run.text:
                #print(run.text)
                run.text=run.text.replace('成佳瑶','张帅')
    savepathname = savepath + '\\' + docxname
    document.save(savepathname)
    print(docxname + "已完成")

print("全部处理完成")