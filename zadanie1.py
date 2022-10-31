from random import randint
import timeit

a = []
for i in range(10):
  a.append(randint(1, 250))

print(a)
b = a.copy()


start_time = timeit.default_timer()
for i in range(len(a) - 1):
  for j in range(len(a) - i - 1):
    if a[j] > a[j+1]:
      a[j],  a[j+1] = a[j+1], a[j]
time1 = timeit.default_timer() - start_time
  
start_time = timeit.default_timer()
b.sort()
time2 = timeit.default_timer() - start_time

print(str(a) + " отсортирован пузырьковой сортировкой за время: " + str(time1) )
print(str(b) + " отсортирован методом sort() за время: " + str(time2))



