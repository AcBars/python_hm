# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from my_functions import rnd_array

def sum_odd(array):
    """The function takes a list as input and outputs the
    sum of the odd elements of the list."""
    sum = 0
    for i in range(1, len(array), 2):
        sum += array[i]
    return sum

list_length = int(input('Введите длину списка: '))
arr = rnd_array(list_length)
result = sum_odd(arr)
print(f'Сумма нечетных элементов массива: {arr}, равна: {result}')