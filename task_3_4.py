# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from my_functions import con_nuber

number_10 = int(input('Введите десятичное число: '))
number_2 = []
while number_10 > 1:
    if number_10 % 2 > 0:
        number_2.append(1)
    else:
        number_2.append(0)
    number_10 //= 2
number_2.append(number_10)
list.reverse(number_2)

number_2 = con_nuber(number_2)
print(number_2)