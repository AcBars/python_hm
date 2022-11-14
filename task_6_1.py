# Задача 1. Создайте программу для игры в "Крестики-нолики".

from random import randint
from my_functions import check_numberint

def pool_print(pool):
    arr = pool.copy()
    for i in range(3):
        arr[i] = ''.join(arr[i])
    print(' _ ' * 3)
    print('\n'.join(arr))    

def step_bot(pool):
    x = randint(0,2)
    y = randint(0,2)
    while pool[x][y] == '|X|' or pool[x][y] == '|0|':
        x = randint(0,2)
        y = randint(0,2)
    pool[x][y] = '|X|'
    step = 1
    return step
    

def check_win(pool, step):
    for i in range(3):
        win = pool[i][0] + pool[i][1] + pool[i][2]
        if win == '|X||X||X|':
            print('Выйграл компьютер!')
            step = 2
            return step
    for i in range(3):
        win = pool[0][i] + pool[1][i] + pool[i][i]
        if win == '|X||X||X|':
            print('Выйграл компьютер!')
            step = 2
            return step
    win = pool[0][0] + pool[1][1] + pool[2][2]
    if win == '|X||X||X|':
            print('Выйграл компьютер!')
            step = 2
            return step
    win = pool[0][2] + pool[1][1] + pool[2][0]
    if win == '|X||X||X|':
            print('Выйграл компьютер!')
            step = 2
            return step
    for i in range(3):
        win = pool[i][0] + pool[i][1] + pool[i][2]
        if win == '|0||0||0|':
            print('Поздравляю! Вы выйграли!')
            step = 2
            return step
    for i in range(3):
        win = pool[0][i] + pool[1][i] + pool[2][i]
        if win == '|0||0||0|':
            print('Поздравляю! Вы выйграли!')
            step = 2
            return step
    win = pool[0][0] + pool[1][1] + pool[2][2]
    if win == '|0||0||0|':
            print('Поздравляю! Вы выйграли!')
            step = 2
            return step
    win = pool[0][2] + pool[1][1] + pool[2][0]
    if win == '|0||0||0|':
            print('Поздравляю! Вы выйграли!')
            step = 2
            return step
    return step

def step_human(pool):
    x = check_numberint(input('Введите строку куда поставить 0: ' ))
    y = check_numberint(input('Введите столбец куда поставить 0: ' ))
    x -= 1
    y -= 1
    if x < 0 or x > 2 or y < 0 or y > 2:
        print('Выпромахнулись! И не попали в поле. Ход переходит компьютеру.')
    else:
        pool[x][y] = '|0|'
    step = 0
    return step

def end_game(arr, step):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '|_|':
                return step
    print('Игра завершена. Свободных полей не осталось')
    step = 2
    return step

pool = []
for i in range(3):
    pool.append([])
    for j in range(3):
        pool[i].append('|_|')
step = randint(0, 1)
if step == 0:
    print('Первым ходит компьютер.')
    step = step_bot(pool)
    pool_print(pool)
else:
    print('Вы ходите первым')
    pool_print(pool)
    step = step_human(pool)
    pool_print(pool)
while step != 2:
    if step == 0:
        step = step_bot(pool)
        step = check_win(pool, step)
        step = end_game(pool, step)
        pool_print(pool)
    else:
        step = step_human(pool)
        step = check_win(pool, step)
        step = end_game(pool, step)
        pool_print(pool)
