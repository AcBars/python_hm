# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , причем чтоб количество элементов было четное.
# Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место и выполнить
# это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from my_functions import check_numberint
from my_functions import rndint_array
import random
import copy

def arr_printtabl(arr):
    temp = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if temp < abs(arr[i][j]):
                temp = abs(arr[i][j])
    temp = len(str(temp))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                arr[i][j] = '0' * (temp + 1)
            elif arr[i][j] > 0:
                arr[i][j] = '+' + '0' * (temp - len(str(arr[i][j]))) + str(arr[i][j])
            else:
                arr[i][j] = '-' + '0' * (temp + 1 - len(str(arr[i][j]))) + str(abs(arr[i][j]))
    for i in range(len(arr)):
        arr[i] = ' | '.join(arr[i])      
    for i in range(len(arr)):
        print(arr[i])
    return

m = check_numberint(input('Введите колличество строк: '))
if m % 2 != 0:
    print('Так как вы ввели не четное число строк, то количество столбцов должно быть четным!')
    n = check_numberint(input('Введите четное число столбцов:'))
    while n % 2 != 0:
        print('Вы ввели не четное число столбцов, количество столбцов должно быть четным!')
        n = check_numberint(input('Введите четное число столбцов:'))
else:
    n = check_numberint(input('Введите колличество столбцов:'))
new_arr = []
for i in range(m):
    new_arr.append(rndint_array(n))
arr = []
arr = copy.deepcopy(new_arr)
arr_printtabl(new_arr)
q = int(m * n / 2)
for l in range(q):
    for i in range(len(arr)):
        for j in range(i, len(arr[i])):
            k = random.randrange(1, len(arr))
            g = random.randrange(len(new_arr) - k -1, len(arr))
            temp = arr[k][g]
            arr[k][g] = arr[i][j]
            arr[i][j] = temp
print('-----------')
arr_printtabl(arr)