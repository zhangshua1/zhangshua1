#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/8/14 22:39 
# @desc: 统计学生成绩

if __name__ == '__main__':
    stu = [['', '', 0, 0] for i in range(5)]

    # 输入五个学生信息
    for i in range(5):
        print('\n请输入第%d个学生的信息:' % (i + 1))
        stu[i][0] = input('stuNo:')
        stu[i][1] = input('name:')
        sum = 0
        # 求出平均成绩
        for j in range(3):
            stu[i][2] = int(input('score %d:' % (j + 1)))
            sum += stu[i][2]
            stu[i][3] = sum // 3.0

    with open('stud', 'w', encoding='utf-8') as fp:  # 打开文件
        print('Sno,Sname,Score,arv', file=fp)
        for i in range(5):
            fp.write('{0},{1},{2},{3}\n'.format(stu[i][0], stu[i][1], stu[i][2], stu[i][3])) # 将学生信息写入文件
    fp.close()  # 关闭文件
