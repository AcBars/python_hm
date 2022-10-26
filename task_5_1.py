# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""

from random import randint
from my_functions import check_numberint

while True :
    answer = input('Привет! Сыграем в игру конфеты?\n')
    answer = answer.lower()
    if answer == 'да':
        count = check_numberint(input('Введите число (от 300 до 3 000) конфет на столе: '))
        while not(count >= 300 and count =< 300=):
            print('Вы ввели число меньше 300 или больше 3000!')
            count = check_numberint(input('Введите число (от 300 до 3 000) конфет на столе: '))
        step = check_numberint(input('Введите максимальное число (от 3 до 30) конфет которое можно взять за один ход: '))
        if not(step > 3 and step <30):
            print('Вы ввели число меньше 3 или больше 30!')
            step = check_numberint(input('Введите максимальное число (от 3 до 30) конфет которое можно взять за один ход: '))
        print('Делаем волшебство определяем кто будет ходить!\n...\n3\n2\n1\n0')
        temp = randint(0,1)
        if temp == 1:
            print('Тебе повезло!\nПерввый ход ваш!')
        else:
            while count > 0:
                print('Сегодня дача на моей стороне первый хожу я!')
                if count % step >= 3:
                    my_step = count % step
                    print('Мой ход! Я беру со стола ' + my_step)
                    count = count - my_step
                    print('На столе осталось ' + count - count % step + ' конфет')
                    print('Ваш ход!')
                    you_step = check_numberint(input('Введите число конфет которое вы возмете со стола: '))
                    if not(you_step >= 3 and you_step <= 30):
                        print('Вы играете не честно! Договорились брать конфет не меньше 3 и не больше 30')
                        you_step = check_numberint(input('Введите число конфет которое вы возмете со стола: '))
                    else:
                        count = count - you_step
                else:
                    my_step = step
                    
                        
    else:
        print('Очень жаль! Надеюсь в следующий раз мы с играем!')
        break
    