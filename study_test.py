from functools import reduce

def f(x):
	return x*x
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(f,L)))

L1 = [x for x in range(1,5)]#1,2,3,4
#reduce 作为参数的函数必须接受两个参数才行，不然会报错。
def f1(x,y):
	return x*y
print(reduce(f1,L1))

#使用递归实现阶乘
def f2(x):
	if x==1:
		return 1
	else:
		return x*f2(x-1)
print(f2(900))
