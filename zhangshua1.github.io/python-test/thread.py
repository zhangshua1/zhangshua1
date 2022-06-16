# Version Python：3.8
# Author Leon

# 导入进程包以及队列包
from multiprocessing import Process,Queue, Lock
import os,sys


def enter(w):
    with open('test.txt','a+') as f:
        f.write('%s'%w)

def test(s,l):
    l.acquire()
    print('子进程开始写%sPID'%s,os.getpid())
    enter(s+'\n')
    print('子进程写结束%sPID'%s,os.getpid())
    l.release()




if __name__ == '__main__':
    locks = Lock()
    p1 = Process(target=test, args=('cool',locks))
    p2 = Process(target=test, args=('hello',locks))
    p3 = Process(target=test, args=('hello2',locks))
    p4 = Process(target=test, args=('hello3',locks))
    p5 = Process(target=test, args=('hello4',locks))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    print('主进程结束')