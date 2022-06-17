#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @author : liuhefei
# @Time : 2019/7/20 10:35 
# @desc:  换分币

if __name__=="__main__":
    # 变量x、y和z分别代表兑换的1元、5角和1角的硬币所具有的钱数（角）
    count = 0  # 计数器
    print("可能的兑换方法如下：")
    # x 为兑换的1元硬币钱数，可能的取值为{0,10,20,30,40,50}
    for x in range(0, 50+1, 10):
        # y为5角硬币钱数，其取值为0,5,10,15,20,25,30,35,40,,45,50
        for y in range(0, 50-x+1, 5):
            # z为1角硬币钱数，其取值为0,1,...50
            for z in range(0, 50-x-y+1, 1):
                if(x + y + z == 50):
                    count += 1
                    if count % 3 == 0:  # 每3列一行
                        print(count, end="   ")
                        print("10*%d+5*%d+1*%d \t" % (x // 10, y // 5, z))
                    else:
                        print(count, end=" ")
                        print("10*%d+5*%d+1*%d \t" % (x // 10, y // 5, z), end=" ")