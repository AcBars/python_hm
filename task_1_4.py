# Задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе
# число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5


from my_functions import check_numberfloat

number_1 = float(check_numberfloat(input('Введите первое вещественное число: ')))
number_2 = float(check_numberfloat(input('Введите второе вещественное число: ')))
sumbol = str(input('Введите символ операции: '))
while not(sumbol == '+' or sumbol == '-' or sumbol == '*' or sumbol == '/' or sumbol == 'mod' or sumbol == 'pow' or sumbol == 'div'):
    print('Вы ввели не поддерживаему операцию!')
    print('Список поддерживаемых операций:')
    print('+, -, /, *, mod, pow, div')
    sumbol = str(input('Введите символ операции: '))
if sumbol == '+':
    print(number_1 + number_2)
elif sumbol == '-':
    print(number_1 - number_2)
elif sumbol == '*':
    print(number_1 * number_2)
elif sumbol == '/':
    if number_2 == 0:
        print('Деление на 0!')
    else:
        print(number_1 / number_2)
elif sumbol == 'mod':
    if number_2 == 0:
        print('Деление на 0!')
    else:
        print(int(number_1 % number_2))
elif sumbol == 'pov':
    print(number_1 ** number_2)
elif sumbol == 'div':
    if number_2 == 0:
        print('Деление на 0!')
    else:
        print(int(number_1 // number_2))