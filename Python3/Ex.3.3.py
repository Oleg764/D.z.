#3.Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
x=[]
A=[1.1, 1.2 ,3.1, 5, 10.01]
for i in  range (5): 
    x.append(round(A[i]-int(A[i]),3))
print (x)
m=x[0]
def xmax(m):

    for i in x:
        if i>m:
            m=i
    return m       
min=x[0]   
def xmin(min):
    
    for i in x:
        if i<min:
            min=i
    return min     
print ('Разница между мах и мин. значением дробной части = ',xmax(m)-xmin(min))
 
