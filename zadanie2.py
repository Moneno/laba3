import math
from random import randint
def f3n(n):
    a,b,c =0,0,0
    for i in range(n):
        a += 1
        b += 2
        c += 3
    return print('Сложность алгоритма 3n', 3*n)
def fnlogn(n):
    a = [randint(1,10) for i in range(n)]
    a.sort()
    print('Cложность алгоритма nlog(n) ',int(n * math.log(n))+1)
def fn(n):
    if n == 0:
        return 1
    for i in range(n):
        num = n*fn(n-1)
    return num
def fnv3(n):
    o = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                o += 1
    print('Cложность алгоритма n^3 ', o)
def f3nlog(n):
    f = randint(1,n)
    b = n
    a = [i for i in range(n)]
    if n % 2 == 0:
        ni = n // 2
    else:
        ni = n // 2 + 1
    for i in range(ni + 1):
        n = len(a)
        if n % 2 == 0:
            if f > a[n // 2 - 1]:
                a = [a[i] for i in range(n // 2, n)]
            else:
                a = [a[i] for i in range(n // 2)]
        if n % 2 != 0:
            if f > a[n // 2]:
                a = [a[i] for i in range(n // 2, n)]
            else:
                a = [a[i] for i in range(n // 2 + 1)]
    print('Cложность алгоритма 3log(n) ', int(3*math.log(b))+1)

n = int(input('введите n '))
f3n(n)
fnlogn(n)
print(f'Сложность алгоритма O(n!) {fn(n)}')
print(f'Cложность алгоритма 3log(n) {fn(n)}')
fnv3(n)
f3nlog(n)