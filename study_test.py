# from functools import reduce
#
# # def f(x):
# # 	return x*x
# # L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(list(map(f, L)))
# #
# # L1 = [x for x in range(1,5)]#1,2,3,4
# # #reduce 作为参数的函数必须接受两个参数才行，不然会报错。
# # def f1(x,y):
# # 	return x*y
# # print(reduce(f1, L1))
# #
# # #使用递归实现阶乘
# # def f2(x):
# # 	if x==1:
# # 		return 1
# # 	else:
# # 		return x*f2(x-1)
# # print(f2(6))
# #
# # #使用reduce实现阶乘
# # def f3(x, y):
# # 	return x * y
# # def Ls(n):
# # 	ls = [x for x in range(1, n)]
# # 	return ls
# #
# # print(Ls(6))
# # L3 = reduce(f3, Ls(6))
# # print(L3)
# #
# # #用map实现把列表的首字母全部大写
# # def normalize(name):
# # 	name = name[0].upper() + name[1:].lower()
# # 	return name
# # print(list(map(normalize, ['admin', 'LISA', 'barT'])))
#
# #用filter筛选出所有奇数
# #
# # """筛选出所有数字"""
# # def create_number():
# # 	n = 1
# # 	while True:
# # 		n = n + 1
# # 		yield n
# #
# # """筛选出奇数"""
# # def jishu(x):
# # 	return x%2==1
# # a = create_number()
# # print(type(a))
# # b = filter(jishu, range(1, 30))
# # c = list(b)
# # print(type(b))
# # print(b)
# # print(c)
# # for i in b:
# # 	if i<20:
# # 		print(i)
# # for i in b:
# # 	if i <10:
# # 		print(i)
# # 	else:
# # 		break
# #滤掉非回数
# # def is_palindrom(n):
# # 	s = str(n)
# # 	return s != s[::-1]
# #
# # print(list(filter(is_palindrom, [1,2,3,4,12321,1234321,123212])))
#
# #用sorted对二维列表排序
#
# # L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('Eale', 100)]
# # def by_name(t):
# #     for n in t:
# #         return n[2]
# # L2 = sorted(L, key=by_name)
# # print(L2)
# # (a))x = [a for a in range(1, 101, 2)]
# # print(x)
# # def bulid(x, y):
# #     return lambda:x+y
# # a = bulid(1, 2)
#
# #装饰器
# # import functools
# # def log(func):
# #     @functools.wraps(func)
# #     def wrapper(*args, **kw):
# #         print("调用装饰器,call %s():" %func.__name__)
# #         return func(*args, **kw)
# #     return wrapper
#
# # #带参数的装饰器
# # def log1(text="test"):
# #
# #     def decorator(func):
# #         @functools.wraps(func)
# #         def wrapper(*args, **kw):
# #             print("开始调用 %s,%s"%(func.__name__, text))
# #             func(*args, **kw)
# #             print("结束调用")
# #         return wrapper
# #     return decorator
# # @log1()
# # def now():
# #     print("wqwqqw")
# #
# #
# # now()
# # print(now.__name__)
#
# #类
# # class Student:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def output(self):
# #         print("姓名是：%s" % self.name)
# #         print("年龄是：%s" % self.age)
# #
# # s = Student("令狐冲", 26)
# # s1 = Student("任盈盈", 18)
# # #s1.name = "任我行"
# # print(s1.name)
# # print(s1.age)
# # @property用法
# # class Screen:
# #     @property
# #     def width(self):
# #         return self._width
# #
# #     @width.setter
# #     def width(self, value):
# #         self._width = value
# #
# #     @property
# #     def height(self):
# #         return self._height
# #
# #     @height.setter
# #     def height(self, value):
# #         self._height = value
# #
# #     @property
# #     def resolution(self):
# #         return self._width * self._height
# #
# # s = Screen()
# # s.width = 1024
# # s.height = 7682
# # print(s.width)
# # print(s.height)
# # print(s.resolution)
# # assert s.resolution == 7866836
#
# #枚举类
# #from enum import Enum, unique
# # Month = Enum('Month', ('Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# # for name, member in Month.__members__.items():
# #     print(name, '==>', member, ',', member.value)
# #
# # Month.Jan=1
#
# # @unique
# # class Weekday(Enum):
# #     Sun = 0
# #     Mon = 1
# #     Tue = 2
# #     Wed = 3
# #     Thu = 4
# #     Fri = 5
# #     Sat = 6
# # print(Weekday.Sun)
# # print(Weekday['Mon'])
# # print(Weekday.Wed.value)
# # print(Weekday(2))
# # print(Weekday.Sun.value > Weekday.Mon.value)
#
# #使用logging记录错误
# # import logging
# # def f(s):
# #     return 10/int(s)
# #
# # def main():
# #     try:
# #         f(0)
# #     except Exception as e:
# #         logging.exception(e)
# #         print("------------------")
# #
# # main()
# # print("end=========")
#
# # def foo(s):
# #     n = int(s)
# #     if n==0:
# #         raise ValueError('invalid value: %s' % s)
# #     return 10 / n
# #
# # def bar():
# #     try:
# #         foo('0')
# #     except ValueError as e:
# #         print('ValueError!:')
# #         raise #把错误向上一级抛
# #
# #
# # bar()
# # import logging
# # logging.basicConfig(level=logging.INFO)
# # s = '0'
# # n = int(s)
# # logging.info('n = %d' % n)
# # print(10 / n)
#
# #super用法
# # class A:
# #     def __init__(self):
# #         print("enter A")
# #         print("leave A")
# #
# #     def run(self):
# #         print("A is running")
# #
# # class B(A):
# #     def __init__(self):
# #         print("enter B")
# #         #A.__init__(self)
# #         #super(B, self).run()
# #         A.run(self)
# #         print("leave B")
# # B()
#
# #序列化：把变量从内存中变为可存储或者可传输的过程。
# #用json序列化
# #import json
# # d = {"age": 20, "score": 88, "name": "Bob"}
# # s = json.dumps(d)
# # print(s)
# # print(type(s))
# # s2 = json.loads(s)
# # print(s2)
# # print(type(s2))
#
# # class Student:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# # s = Student("Bob", 25)
# # s1 = json.dumps(s, default=lambda obj: obj.__dict__)
# # print(s1)
# # print(type(s1))
# # s2 = json.loads(s1)
# # print(s2)
# # print(type(s2))
#
# # # 多进程
# # from multiprocessing import Process
# # import os
# # def run_proc(name):
# #     print("Child process %s (%s)" %(name, os.getpid()))
# #
# # if __name__ == '__main__':
# #     print("Parent process %s" %os.getpid())
# #     p = Process(target=run_proc, args=("test",))
# #     print("child process will start")
# #     p.start()
# #     p.join()
# #     print("child process end")
#
#启动大量子进程用pool
# from multiprocessing import Pool
# import os, time, random
# def long_time_task(name):
#     print("Run task %s (%s)..." % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#
#     end = time.time()
#     print('Task %s run %0.2f seconds' % (name, (end - start)))
# if __name__ == '__main__':
#
#     print("Parent process %s." % os.getpid())
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print("Waiting for all subprocess done...")
#     p.close()
#     p.join()
#     print("All subprocess done..")
# #多线程
# #import time,threading
# #线程执行的代码
# # def loop():
# #     print("thread %s is running..." %threading.current_thread().name)
# #     n = 0
# #     while n < 5:
# #         n = n + 1
# #         print("thread %s >>> %s" %(threading.current_thread().name, n))
# #         time.sleep(1)
# #     print("thread %s ended" %threading.current_thread().name)
# # print('thread %s is running...'%threading.current_thread().name)
# # t = threading.Thread(target=loop, name='LoopThread')
# # t.start()
# # t.join()
# # print("thread %s ended"%threading.current_thread().name)
#
# # #多线程加锁的
# # # 假定这是你的银行存款:
# # balance = 0
# # lock = threading.Lock()
# #
# # def change_it(n):
# #     # 先存后取，结果应该为0:
# #     global balance
# #     balance = balance + n
# #     balance = balance - n
# #
# # def run_thread(n):
# #     for i in range(100000):
# #         #先获取锁
# #         lock.acquire()
# #
# #         try:
# #             #放心的改吧
# #             change_it(n)
# #         finally:
# #             #释放锁
# #             print("释放锁"+ str(i))
# #             lock.release()
# #
# #
# # t1 = threading.Thread(target=run_thread, args=(5,), name="run_thread1")
# # t2 = threading.Thread(target=run_thread, args=(8,), name="run_thread2")
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# # print(balance)
#
# # #多线程全局变量
# # import threading
# # #创建全局ThreadLocal对象
# # local_school = threading.local()
# # local_school.name = 'local_data21'
# # def process_student():
# #     # 获取当前线程类的student
# #     std = local_school.student
# #     print("Hello, %s (in %s)"%(std, threading.current_thread().name))
# #
# # def process_thread(name):
# #     local_school.student = name
# #     print("Hello, %s (in %s)" % (local_school.student, threading.current_thread().name))
# #     process_student()
# #
# # t1 = threading.Thread(target=process_thread, args=('Alice',), name="Thead-A")
# # t2 = threading.Thread(target=process_thread, args=('Bob',), name="Thead-B")
# # print("Hello, %s (in %s)"%(local_school.name, threading.current_thread().name))
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
#
# import threading
# def print_n(name):
#     print("I am %s, my thread_name is %s" % (name, threading.current_thread().name))
#
# threads = []
# t1 = threading.Thread(target=print_n,args=('张三丰',), name='Thread-t1')
# t2 = threading.Thread(target=print_n, args=('杨潇',), name='Thread-t2')
# threads.append(t1)
# threads.append(t2)
# for t in threads:
#     t.start()
#     t.join()
# print("all thread end")
# """进程间通信"""
# from multiprocessing import Process, Queue
# import os, time, random, multiprocessing
# #写数据进程执行的代码
# def write(q):
#     print('Process to read: %s and my father is %s' % (os.getpid(), os.getppid()))
#     for value in ['A', 'B', 'C', 'D']:
#         print('Puts %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读取数据进程执行的代码
# def read(q):
#     print('Process to read: %s and my father is %s' % (os.getpid(), os.getppid()))
#     while True:
#         wq = q.get()
#         print('Get %s from queue.' % wq)
#
# #父进程创建Queue，并传给各个子进程
# if __name__ == '__main__':
#     q = Queue()
#     print('Parent process is %s' % os.getpid())
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     #启动子进程pw，写入
#     pw.start()
#     #启动子进程pr，读取
#     pr.start()
#     #等待pw结束
#     pw.join()
#     #pr是死循环，无法等待其结束，只能强制结束
#     pr.terminate()

# """分布式进程"""
# import random, time, queue
# from multiprocessing.managers import BaseManager
# #发送任务的队列
# task_queue = queue.Queue()
# #接收任务的队列
# result_queue = queue.Queue()
#
# #从BaseManager继承的QueueManager
# class QueueManager(BaseManager):
#     pass
# #把两个Queue注册到网络上
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_task', callable=lambda: result_queue)
# #绑定端口5000，设置验证码‘abc‘
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# #启动queue
# manager.start()
# #获取通过网络访问的Queue对象
# task = manager.get_task_queue()
# result = manager.get_result_task()
# #放几个任务进去
# for i in range(10):
#     n = random.randint(0, 1000)
#     print('Put task %d' % n)
#     task.put(n)
#
# #从result队列获取结果
# print('Try get results..')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# #关闭
# manager.shutdown()
# print('master exit.')

# import re
# t = input("请输入一个网址:")
# s = re.compile(r'[0-9a-zA-Z]+[.][0-9a-zA-Z]+[.][0-9a-zA-Z]+')
# if s.match(t):
#     print("pass")
# else:
#     print("请重新输入")
#
# """上下文优化"""
# from contextlib import contextmanager
#
# class Query(object):
#
#     def __init__(self):
#         self.name = 'wangqi'
#         print('this is __init__')
#
#     def __enter__(self):
#         print('Enter')
#         return self
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('End')
# with Query() as wq:
#     wq.query()

# @contextmanager
# def creat_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
#
# with creat_query('Bob') as q1:
#     q1.query()

"""解析xml"""
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('start_element:%s, attrs:%s' %(name, str(attrs)))

    def end_element(self, name):
        print('end_element:%s' % name)

    def char_data(self, text):
        a = []
        a.append(text)
        #print('char_data:%s' % text)
        return a
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
    <li><a href="/java">Java</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


print('==============')
print(handler)


