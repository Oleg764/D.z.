#4. Задана натуральная степень k.
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
#многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
import itertools

k =int (input('Введите степень k  :'))

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios
print(get_ratios(k))
def get_polynom(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynom(k, ratios)
print(polynom1)

with open('C:\Python\Python4\Polynomial.txt', 'w') as data:
    data.write(polynom1)


# Второй многочлен для следующей задачи:

k = 2

ratios = get_ratios(k) 
polynom2 = get_polynom(k, ratios)
print(polynom2)

with open('C:\Python\Python4\Polynom2.txt', 'w') as data:
    data.write(polynom2)