#Лабораторная 1, 1.1. Операторы и функции, Вариант 2, 3 задача

import math

h = int(input('Введите h: '))

a = math.sqrt(((math.fabs(math.sin(18*h)))+17)/((1-math.sin(4*h))**2));
b = 1-(math.sqrt(3/(3+math.fabs(math.cos(a*h*h)-math.sin(a*h)))));
c = a*h*h*math.sin(b*h)+(b*h*h*h)*math.cos(a*h);

if ((b*b) - (4*a*c) >= 0):
    print('Корни есть')
else:
    print('Корней нет')