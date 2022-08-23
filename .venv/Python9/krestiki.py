from tkinter import *
import random
root = Tk()
root.title('Крестики-нолики')
root.iconbitmap("C:\Python\.venv\изображение_2022-08-23_134411331.ico")
game_run = True
field = []
cross_count = 0       # библиотеки и объявление переменных
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')
def check_win(s):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], s)
        check_line(field[0][n], field[1][n], field[2][n], s)
    check_line(field[0][0], field[1][1], field[2][2], s)
    check_line(field[2][0], field[1][1], field[0][2], s)

def check_line(a1,a2,a3,s):
    if a1['text'] == s and a2['text'] == s and a3['text'] == s:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global game_run
        game_run = False                                        #    Проверка победы       
def can_win(a1,a2,a3,s):
    res = False
    if a1['text'] == s and a2['text'] == s and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == s and a2['text'] == ' ' and a3['text'] == s:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == s and a3['text'] == s:
        a1['text'] = 'O'
        res = True
    return res
def computer_move():
    while game_run == True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break                                                     #        Действия компьютера
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,font=('Verdana', 20, 'bold'),background='lavender',command=lambda row =row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
root.mainloop()                                                       #    Графический интерфейс