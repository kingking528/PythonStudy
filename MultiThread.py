#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
import time, threading
# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
"""

#多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
#多线程中，所有变量都由所有线程共享，任何一个变量都可以被任何一个线程修改
# 线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
import time, threading
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(x,n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(x,n):  #没有锁的方法
    for i in range(1000000):
        change_it(x,n)

def locked_thread(x,n):
    for i in range(1000000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(x,n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
start = time.time()
t1 = threading.Thread(target=run_thread, args=(1,5,))
t2 = threading.Thread(target=run_thread, args=(2,8,))
t3 = threading.Thread(target=run_thread, args=(3,13,))
t4 = threading.Thread(target=run_thread, args=(4,17,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
end = time.time()
print(balance)
print('Task runs %0.5f seconds.' % (end - start))

# 创建全局ThreadLocal对象:解决多个线程各自处理数据的问题
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()