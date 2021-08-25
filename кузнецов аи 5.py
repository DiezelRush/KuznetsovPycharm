#Лабораторная 1, 1.1. Операторы и функции, Вариант 4, 2 задача
import math

y = float(input('Введите y:'))

for x in range(8, 34, 1):
    x = x/10
    z = (((y - x) ** 2) / 2) + (((math.fabs(y - x)) ** 3) / 3)
    print (z)



