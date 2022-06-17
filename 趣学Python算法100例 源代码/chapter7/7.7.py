#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/13 10:16 
# @desc: 24点

op = ['#', '+', '-', '*', '/']


def cal(x, y, op):
    if op == 1:
        return x + y  # op等于1，加法运算
    elif op == 2:
        return x - y  # op等于2，减法运算
    elif op == 3:
        return x * y  # op等于3，乘法运算
    elif op == 4:
        return x / y  # op等于4，除法运算


# 对应的表达式类型：((A□B)□C)□D
def calculate_model1(i, j, k, t, op1, op2, op3):
    r1 = cal(i, j, op1)
    r2 = cal(r1, k, op2)
    r3 = cal(r2, t, op3)
    return r3


# 对应的表达式类型：(A□(B□C))□D
def calculate_model2(i, j, k, t, op1, op2, op3):
    r1 = cal(j, k, op2)
    r2 = cal(i, r1, op1)
    r3 = cal(r2, t, op3)
    return r3


# 对应的表达式类型：A□(B□(C□D))
def calculate_model3(i, j, k, t, op1, op2, op3):
    r1 = cal(k, t, op3)
    r2 = cal(j, r1, op2)
    r3 = cal(i, r2, op1)
    return r3


# 对应的表达式类型：A□((B□C)□D)
def calculate_model4(i, j, k, t, op1, op2, op3):
    r1 = cal(j, k, op2)
    r2 = cal(r1, t, op3)
    r3 = cal(i, r2, op1)
    return r3


# 对应的表达式类型：(A□B)□(C□D)
def calculate_model5(i, j, k, t, op1, op2, op3):
    r1 = cal(i, j, op1)
    r2 = cal(k, t, op3)
    r3 = cal(r1, r2, op2)
    return r3


# 函数get24用于寻找符合要求（计算结果为24）的表达式
def get24(i, j, k, t):
    flag = False
    for op1 in range(1, 5):
        for op2 in range(1, 5):
            for op3 in range(1, 5):
                # 找到((A□B)□C)□D类型的表达式中符合要求的那些表达式
                if calculate_model1(i, j, k, t, op1, op2, op3) == 24:
                    print("((%d%c%d)%c%d)%c%d=24" % (i, op[op1], j, op[op2], k, op[op3], t))
                    flag = True

                # 找到(A□(B□C))□D类型的表达式中符合要求的那些表达式
                if calculate_model2(i, j, k, t, op1, op2, op3) == 24:
                    print("(%d%c(%d%c%d))%c%d=24" % (i, op[op1], j, op[op2], k, op[op3], t))
                    flag = True

                # 找到A□(B□(C□D))类型的表达式中符合要求的那些表达式
                if calculate_model3(i, j, k, t, op1, op2, op3) == 24:
                    print("%d%c(%d%c(%d%c%d))=24" % (i, op[op1], j, op[op2], k, op[op3], t))
                    flag = True

                # 找到A□((B□C)□D)类型的表达式中符合要求的那些表达式
                if calculate_model4(i, j, k, t, op1, op2, op3) == 24:
                    print("%d%c((%d%c%d)%c%d)=24" % (i, op[op1], j, op[op2], k, op[op3], t))
                    flag = True

                # 找到(A□B)□(C□D)类型的表达式中符合要求的那些表达式
                if (calculate_model5(i, j, k, t, op1, op2, op3) == 24):
                    print("(%d%c%d)%c(%d%c%d)=24" % (i, op[op1], j, op[op2], k, op[op3], t))
                    flag = True

    return flag

if __name__ == '__main__':
    print("Please input four integer (1~10)")
    i, j, k, t = map(int, input().split())
    # 若输入数值不合法，重新输入
    if i < 1 or i > 10 or j < 1 or j > 10 or k < 1 or k > 10 or t < 1 or t > 10:
        print("Input illege, Please input again")
        i, j, k, t = map(int, input().split())

    if get24(i, j, k, t):  # 找到符合要求的表达式
        pass
    else:
        print("Sorry, the four integer cannot be calculated to get 24")

