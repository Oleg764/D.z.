

#3.Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной 
#последовательности.

from random import randint

def num_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = num_list(size, m, n)
print(origin)
print(unic_value(origin))

