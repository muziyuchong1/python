# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

# 1在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0 (n=0)
# F1 = 1 (n=1)
# Fn = F[n-1]+ F[n-2](n>=2)

#方法1
def fib(n):
    a,b = 1,1
    for i in range(2,n):
        a,b = b,a+b
    return a
print(fib(3))


#方法2 使用装饰器加上缓存
from functools import lru_cache

@lru_cache(None)
def fib(n):
    assert n >=0
    return n if n<=1 else fib(n-1) + fib(n-2)

print(fib(4))

