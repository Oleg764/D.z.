

import random

begin = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
    'Основные правила игры: '
    'Нам будет дано некоторое количество конфет, '
    'за один ход мы можем взять не более  28 конфет '
    'Итак, начнём!')
def enter_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'Ботик'
    print(f'Очень приятно {player1}, меня зовут {player2}')
    
    return [player1, player2]  

def game(n, m, players):
    count = pl
    while n > 0:
        if not count %2:
            hod = random.randint(1,m)
            print(f'Ботик забирает {hod}')
        else:    
            print(f'возьмите конфеты {players[0]} ' )
            hod = int(input())
            if hod > n or hod > m and hod !=" ":
                print(f'Это слишком много, можно взять не более {m} конфет, у нас всего {n} конфет')
                attempt = 3
                while attempt > 0:
                    if n >= hod <= m:
                         break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    hod = int(input())
                    attempt -=1
                else: 
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')  
        n = n -hod
        if n > 0:
             print(f'Осталось {n} конфет ')
        else:
             print('Все конфеты разобраны.')
        count +=1
    return players[ count%2]

print(begin)
players = enter_players()

n = int(input('Сколько конфет будем разыгрывать?\n '))
m = 28
pl = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую цифру\n'))
if pl != 1:
        pl = 0        
winer = game(n, m, players)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')