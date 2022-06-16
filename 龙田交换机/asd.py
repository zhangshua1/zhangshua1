#!/usr/bin/python3

from threading import Thread,Lock
import time
import xlsxwriter

num = 0
lock=Lock()
def nu1():
    global num
    for i in range(100000):
        lock.acquire()
        num+=1
        lock.release()
    print('nu1的值是：',num)
def nu2():
    global num
    for i in range(100000):
        lock.acquire()
        num+=1
        lock.release()
    print('nu2的值是：',num)

if __name__ == "__main__":
    print('开始运行')
    t1 = Thread(target=nu1)
    t2 = Thread(target=nu2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# exitFlag = 0

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)

# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")