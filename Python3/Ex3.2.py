#2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

a = [3, 6, 7, 23, 45, 67, 2]
print('Произведение пар чисел списка [3, 6, 7, 23, 45, 67, 2] = ', end='')
for i in range(1, 8):
    c = a[-i]*a[i-1]
    print(c, end=' , ')
    if a[-i] == a[i-1]:
        break