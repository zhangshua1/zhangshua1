#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/9 1:09 
# @desc: 马踏棋盘

# 找到基于x,y位置的下一个可走的位置
def nextxy(x, y, count):
    if count == 0 and x + 2 <= X - 1 and y - 1 >= 0 and chess[x + 2][y - 1] == 0:  # 找到坐标(x+2,y-1)
        x = x + 2
        y = y - 1
        flag = True

    elif count == 1 and x + 2 <= X - 1 and y + 1 <= Y - 1 and chess[x + 2][y + 1] == 0:  # 找到坐标(x+2,y+1)
        x = x + 2
        y = y + 1
        flag = True

    elif count == 2 and x + 1 <= X - 1 and y - 2 >= 0 and chess[x + 1][y - 2] == 0:  # 找到坐标(x+1,y-2)
        x = x + 1
        y = y - 2
        flag = True

    elif count == 3 and x + 1 <= X - 1 and y+2 <= Y-1 and chess[x+1][y+2] == 0:  # 找到坐标(x+1,y+2)
        x = x + 1
        y = y + 2
        flag = True

    elif count == 4 and x - 2 >= 0 and y - 1 >= 0 and chess[x - 2][y - 1] == 0:  # 找到坐标(x-2,y-1)
        x = x - 2
        y = y - 1
        flag = True

    elif count == 5 and x - 2 >= 0 and y + 1 <= Y - 1 and chess[x - 2][y + 1] == 0:  # 找到坐标(x-2,y+1)
        x = x - 2
        y = y + 1
        flag = True

    elif count == 6 and x - 1 >= 0 and y - 2 >= 0 and chess[x - 1][y - 2] == 0:  # 找到坐标(x-1,y-2)
        x = x - 1
        y = y - 2
        flag = True

    elif count == 7 and x - 1 >= 0 and y + 2 <= Y - 1 and chess[x - 1][y + 2] == 0:  # 找到坐标(x-1,y+2)
        x = x - 1
        y = y + 2
        flag = True

    else:
        flag = False

    return flag, x, y

# 深度优先搜索地"马踏棋盘"
def TravelChessBoard(x, y, tag):
    x1, y1, flag, count = x, y, False, 0
    chess[x][y] = tag
    if tag == 60:  # 搜索成功，返回1
        return True
    flag, x1, y1 = nextxy(x1, y1, count)  # 找到基于(x1,y1)的下一个可走位置
    while not flag and count < 7:  # 上一步未找到，则在其余几种可走位置中寻找下一个可走位置
        count = count + 1
        # print('(1): ', count)
        flag, x1, y1 = nextxy(x1, y1, count)

    while flag:  # 找到下一个可走位置，则进行深度优先搜索
        if TravelChessBoard(x1, y1, tag + 1):  # 递归
            return True
        x1 = x
        y1 = y
        count = count + 1
        flag, x1, y1 = nextxy(x1, y1, count)  # 寻找下一个(x,y)
        while not flag and count < 7:  # 循环地寻找下一个(x,y)
            count = count + 1
            # print('(2): ', count)
            flag, x1, y1 = nextxy(x1, y1, count)

    if not flag:
        chess[x][y] = 0  # 搜索不成功，擦除足迹，返回0
    return False


if __name__ == '__main__':
    X = 8
    Y = 8
    chess = [[0]*X for i in range(Y)]  # 初始化，棋盘的所有位置都置0

    if TravelChessBoard(2, 0, 1):  # 深度优先搜索
        for i in range(X):
            for j in range(Y):
                print("%-5d" % chess[i][j], end='')
            print()
        print("The horse has travelled the chess borad")
    else:
        print("The horse cannot travel the chess board")

