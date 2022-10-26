# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""

from random import randint
from my_functions import check_numberint

def us_progres(step):
    """Request the user's progress (Запрос хода у пользователя)."""
    print('Ваш ход!')
    you_step = check_numberint(input('Введите число конфет которое вы возмете со стола: '))
    while not(you_step > 0 and you_step <= step):
        print(f'Вы играете не честно! Договорились брать конфет нне больше {step}')
        you_step = check_numberint(input('Введите число конфет которое вы возмете со стола: '))
    return you_step

while True :
    answer = input('Привет! Сыграем в игру конфеты?\n')
    answer = answer.lower()
    if answer == 'да':
        count = check_numberint(input('Введите число (от 300 до 3 000) конфет на столе: '))
        while not(count >= 300 and count <= 3000):
            print('Вы ввели число меньше 300 или больше 3000!')
            count = check_numberint(input('Введите число (от 300 до 3 000) конфет на столе: '))
        step = check_numberint(input('Введите максимальное число (от 3 до 30) конфет которое можно взять за один ход: '))
        while not(step >= 3 and step <=30):
            print('Вы ввели число меньше 3 или больше 30!')
            step = check_numberint(input('Введите максимальное число (от 3 до 30) конфет которое можно взять за один ход: '))
        print('Делаем волшебство определяем кто будет ходить!\n...\n3\n2\n1\n0')
        temp = randint(0,1)
        if temp == 1:
            print('Сегодня вам повезло!\nПерввый ход ваш!')
            while count > 0:
                count = count - us_progres(step)
                if count == 0:
                    print('Вы выйграли!')
                    break
                print(f'На столе осталось {count} конфет')
                if count % (step + 1) >= 1:
                    my_step = count % (step + 1)
                    print(f'Мой ход! Я беру со стола {my_step} конфет')
                    count = count - my_step
                    if count == 0:
                        print('Я выйграл!')
                        break
                    print(f'На столе осталось {count} конфет')
                else:
                    my_step = step
                    print(f'Мой ход! Я беру со стола {my_step} конфет')
                    count = count - my_step
                    if count == 0:
                        print('Я выйграл!')
                        break
                    print(f'На столе осталось {count} конфет')
        else:
            print('Сегодня удача на моей стороне первый хожу я!')
            while count > 0:
                if count % (step + 1) >= 1:
                    my_step = count % (step + 1)
                    print(f'Мой ход! Я беру со стола {my_step} конфет')
                    count = count - my_step
                    if count == 0:
                        print('Я выйграл!')
                        break
                    print(f'На столе осталось {count} конфет')
                else:
                    my_step = step
                    print(f'Мой ход! Я беру со стола {my_step} конфет')
                    count = count - my_step
                    if count == 0:
                        print('Я выйграл!')
                        break
                    print(f'На столе осталось {count} конфет')
                count = count - us_progres(step)
                if count == 0:
                    print('Вы выйграли!')
                    break
                print(f'На столе осталось {count} конфет')
        break                     
    else:
        print('Очень жаль! Надеюсь в следующий раз мы с играем!')
        break
    