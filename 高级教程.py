'''
正则表达式 import re
'''

import re
print(re.match('www','www.baidu.com').span()) #在起始位置匹配
print(re.match('com','www.baidu.com')) #不在其实位置匹配

#Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，
# 可以在字符串前面添加一个 r，表示原始字符串

line = "Cats are smarter than dogs"
#re.M:多行匹配
#re.I:使匹配对大小写不敏感
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print('matchObj.group():',matchObj.group())
    print('matchObj.group(1):',matchObj.group(1))
    print('matchObj.group(2):',matchObj.group(2))
    print('matchObj.groups():',matchObj.groups())
else:
    print('没有匹配')

'''
python pass :空语句，为了保持程序结构的完整性，pass不做任何事情，只用作占位语句
'''

'''
多线程:使用threading模块来创建线程

线程同步:通过threading.Lock()获取锁对象，Lock.acquire() 获取锁，Lock.release() 释放锁
'''
import threading
import time

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('线程开始：',self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        printThreadInfo(self.name,self.counter,2)
        #释放锁
        threadLock.release()
        print('线程结束：',self.name)


def printThreadInfo(threadName,counter,delay):

    while counter:
#        time.sleep(delay)
        print('%s:%s' % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()


#创建新的线程
thread1 = myThread(1,'thread-1',3)
thread2 = myThread(2,'thread-2',3)

#开启线程
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('退出主线程')

'''
队列：Queue
'''

'''
json:对json数据进行转换
'''

'''
日期和时间
'''

print('当前时间：',time.localtime())

help(thread1)

import sys
print(sys.version_info)

'''
assert 断言：可以理解为我断言expression表达式为真，如果为假，就抛出异常AssertionError
             类似于 raise if not
用法：assert expression [, arguments](可选的表达式)
'''

assert_test = 'str'

assert isinstance(assert_test,str) ,repr(assert_test)


