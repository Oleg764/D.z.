#3.Создайте программу для игры в ""Крестики-нолики"".
import random
maps = [1,2,3,
        4,5,6,
        7,8,9]
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Вы"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Комп"              
    return win
# Основная программа
game_over = False
human = True
rt=[1,2,3,4,5,6,7,8,9]
while game_over == False:
    print_maps()
    if human == True and rt!=[]:
        symbol = "X"
        step = int(input("Человек, ваш ход: "))
        rt.remove(step)
    else:
        if rt != []:
            print("Компьютер делает ход: ")
            symbol = "O"
            step = random.choice(rt)
            rt.remove(step)
        else:
            print('ничья')
            break
    if step != "":
        step_maps(step,symbol) 
        win = get_result() # определим победителя
        if win != "":
            game_over = True
        else:
            game_over = False
    human = not(human)                
print_maps()
print("Победил", win) 