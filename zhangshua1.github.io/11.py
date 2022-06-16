# name = input("请输入你的名字：")
# age = int(input("请输入你的年龄："))
# add = input("住址：")
# s = f"我叫{name}，我今年{age}，我住在{add}"
# print(s)

# s = "s a d a s f"
# print(s.upper())

# lst = ["王丽","王五","里斯","张三"]
# for item in lst:
#     print (item)
# print(len(lst))
# print(lst[::-1])
# print(lst[1])

#把所有姓张的改成姓王
# lst=["张三","李四","王五","张无忌","武则天","恺"]
# for i in range(len(lst)):
#     item = lst[i]
#     if item.startswith("张"):
#         new_name = "王"+item[1:]
#         lst[i] = new_name
# print(lst)

# with open("dog.jpg", mode="rb") as f1, \
#      open("dog2.jpg", mode="wb") as f2:
#      for line in f1:
#          f2.write(line)


for i in range(65536):
    print(chr(i)+" ", end="")



















