#Лабораторная 1, 1.1. Операторы и функции, Вариант 1, 5 задача
import math

a = int(input('Введите a: '))
n = int(input('Введите n: '))

1# for: a*(a+1)*(a+2)*...*(a+n-1)
s = 1
for i in range(a, n + a):
    s *= i
print(s)

