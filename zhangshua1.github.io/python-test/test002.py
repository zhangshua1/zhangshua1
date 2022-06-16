# a = input("please input a shuzi:")
# print("my name is %s" % a)
a = "abcdef"
print(a[2])
print(a.find("c"))
b = ['zhangsan','lisi','wangwu']
print(b.index('lisi'))
print('lisi' in b)
b.append('shuai')
print(b)
print(b[3])
i = 0
while i < len(b):
    print(b[i])
    i += 1
for i in b:
    print(i)