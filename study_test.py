from functools import reduce

# def f(x):
# 	return x*x
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(map(f, L)))
#
# L1 = [x for x in range(1,5)]#1,2,3,4
# #reduce 作为参数的函数必须接受两个参数才行，不然会报错。
# def f1(x,y):
# 	return x*y
# print(reduce(f1, L1))
#
# #使用递归实现阶乘
# def f2(x):
# 	if x==1:
# 		return 1
# 	else:
# 		return x*f2(x-1)
# print(f2(6))
#
# #使用reduce实现阶乘
# def f3(x, y):
# 	return x * y
# def Ls(n):
# 	ls = [x for x in range(1, n)]
# 	return ls
#
# print(Ls(6))
# L3 = reduce(f3, Ls(6))
# print(L3)
#
# #用map实现把列表的首字母全部大写
# def normalize(name):
# 	name = name[0].upper() + name[1:].lower()
# 	return name
# print(list(map(normalize, ['admin', 'LISA', 'barT'])))

#用filter筛选出所有奇数
#
# """筛选出所有数字"""
# def create_number():
# 	n = 1
# 	while True:
# 		n = n + 1
# 		yield n
#
# """筛选出奇数"""
# def jishu(x):
# 	return x%2==1
# a = create_number()
# print(type(a))
# b = filter(jishu, range(1, 30))
# c = list(b)
# print(type(b))
# print(b)
# print(c)
# for i in b:
# 	if i<20:
# 		print(i)
# for i in b:
# 	if i <10:
# 		print(i)
# 	else:
# 		break
#滤掉非回数
# def is_palindrom(n):
# 	s = str(n)
# 	return s != s[::-1]
#
# print(list(filter(is_palindrom, [1,2,3,4,12321,1234321,123212])))

#用sorted对二维列表排序

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('Eale', 100)]
# def by_name(t):
#     for n in t:
#         return n[2]
# L2 = sorted(L, key=by_name)
# print(L2)
# (a))x = [a for a in range(1, 101, 2)]
# print(x)
# def bulid(x, y):
#     return lambda:x+y
# a = bulid(1, 2)

#装饰器
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print("调用装饰器,call %s():" %func.__name__)
#         return func(*args, **kw)
#     return wrapper

# #带参数的装饰器
# def log1(text="test"):
#
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print("开始调用 %s,%s"%(func.__name__, text))
#             func(*args, **kw)
#             print("结束调用")
#         return wrapper
#     return decorator
# @log1()
# def now():
#     print("wqwqqw")
#
#
# now()
# print(now.__name__)

#类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        print("姓名是：%s" % self.name)
        print("年龄是：%s" % self.age)

s = Student("令狐冲", 26)
s1 = Student("任盈盈", 18)
#s1.name = "任我行"
print(s1.name)
print(s1.age)