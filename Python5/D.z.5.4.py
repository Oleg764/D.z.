#4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных файлах
file1='1.txt'
file2='2.txt'

with open(file1, 'r+') as data:
      txt1=  data.read()
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res
str1 =  coding(txt1)   
print(str1)
with open(file2, 'w') as data:
    str1=  data.write(str1)    
def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res
print(decoding(coding(txt1)))   



       