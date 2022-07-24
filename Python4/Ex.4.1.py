# 30. Вычислить число pi c заданной точностью d
# 	  Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)
d=input()
def dCount(f):
    if "." in f:
         return len(f.split(".")[1].rstrip("0"))
    else:
         return 0
d =int( dCount(d) )      
k = 1
s = 0
for i in range ( 10000000 ):
    if i % 2== 0 :
        s += 4 / k
    else :
        s -= 4 / k
    k += 2
print (round(s,d))