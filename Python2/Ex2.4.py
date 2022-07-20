#5.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#Позиции вводятся пользователем

N = int(input('Введите число  n : '))
numbers =[]
for i in range(-N, N+1):
    N= -N +1    
    numbers.append(i)

print (numbers)
int_list = []
for element in input('Введите 2 номера позиций через пробел  : ').split():
    int_list.append(int(element))
    composition=1
    composition*=numbers[int_list[element]]
    

#for element in range[0:-1]:
    
    #composition_elem*=int(numbers[int_list[element]])
#composition_elem =numbers[int_list [0]]*numbers[int_list [1]]
#print ('Произведение элементов = ',composition_elem)
print (composition)