import sys
sys.setrecursionlimit(3000)
def fact(n):
    if n== 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(2000))

import sys
sys.setrecursionlimit(3000)

from functools import lru_cache

@lru_cache()
def F(n):
    if n<=1:
        return n
    elif n % 4 ==0:
        return n + F(n/4 - 1)
    else:
        return -1*10**30

for i in range(1, 10000):
    if F(i)>2000:
        print(i)
        break


def f(i,finish):
    if i<finish:
        return 0
    elif i==finish:
        return 1
    else:
        return f(i-1, finish)+f(i-3, finish)+ f(i//3,finish)

print(f(22,2))