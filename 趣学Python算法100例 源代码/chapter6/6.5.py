#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# author:liuhefei
# desc: 新郎和新娘

if __name__ == "__main__":
    # 三个新郎为A、B、C，三个新娘为X、Y、Z
    groom = ['A', 'B', 'C']  # 定义新郎列表

    # 穷举所有可能情况
    for x in groom:
        for y in groom:
            for z in groom:
                # 新郎A的新娘不是X，那就只能是Y和Z;
                # X的新郎不是C,那就只能是A和B;
                # C的新娘不是Z,那就只能是X和Y；
                # 由此推测出：新郎C的新娘是Y,那么新郎A的新娘是Z,进一步新郎B的新娘是X
                if x != groom[0] and x != groom[2] and z != groom[2] and x != y and x != z and y != z:
                    print("结果为：")
                    print("新娘X与新郎" + x + "结婚");
                    print("新娘Y与新郎" + y + "结婚");
                    print("新娘Z与新郎" + z + "结婚");

