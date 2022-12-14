import math
def f1(n):
    print('алгоритм поиска полследнего элемента в массиве')
    a = [int(input(f'введите {i+1} элемент массива ')) for i in range(n)]
    f = a[-1]
    print(f'последний элемент массива {f}')
    print('в алгоритмах сложностью  О(1) количество шагов линейно зависит от количества элементов, сложность данного алгоритма 1')
def flogn( A, n, value ):
    if n == 1:
        if A[ 0 ] == value:
            return True
        else:
            return False
    if value < A[ n // 2 ]:
        return flogn( A[ 0:( n / 2 - 1 ) ], n / 2 - 1, value )
    elif value > A[ n // 2 ]:
        return flogn( A[ ( n / 2 + 1 ):n ], n / 2 - 1, value )
    else:
        return True
def fn2(n):
    a = 0
    for i in range(n):
        for j in range(n):
            a += 1
    print(a)
def f2n(n):
    if n <= 1: return n
    return f2n(n-2) + f2n(n-1)

s = input()
if s == '1':
    n = int(input('введите количество элементов в массиве '))
    f1()
if s == '2':
    print('алгоритм бинарного поиска')
    n, value = map(int, input('Введите количество элементов массива и искомый элемент ').split())
    A = [int(input(f'введите {i+1} элемент массива ')) for i in range(n)]
    print(flogn( A, n, value ))
    print('в алгоритмах сложностью  О(logn) количество шагов логарифмически зависит от количества элементов, сложность алгоритма при введенных значениях ', math.log(n))
if s == '3':
    print('цикл в цикле')
    n = int(input('Введите n'))
    fn2()
    print('в алгоритмах сложностью  О(n^2) количество шагов квадратично зависит от количества элементов, сложность алгоритма при введенных значениях ',n*n)
if s == '4':
    print('алгоритм рекрсивного расчета чисел фибоначи')
    n = int(input('Введите какое по номеру число найти '))
    print(f'Это число {f2n(n)}')
    print('в алгоритмах сложностью  О(2^n) количество шагов экспоненциально зависит от количества элементов, сложность алгоритма при введенных значениях ',2**n)