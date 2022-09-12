# 1 - Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

def check_number (number):
    while type: 
        try:
            number = float(number)      
            return number
        except ValueError:
            print('Вы ввели не вещественное число! ')
            number = input('Введите вещественное число: ')
number = float(check_number (input('Введите вещественное число: ')))

def sum_number (number):
    if number < 0:
        number *= -1
    number = str(number)
    list_numbers = list(number)
    list_numbers.remove('.')
    list_numbers = [int(x) for x in list_numbers]
    summa = sum(list_numbers)
    return summa

print(sum_number (number))