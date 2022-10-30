# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 

#     [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]

from my_functions import rndint_array
import re

lst_arr = rndint_array(10, 95, 100)
print(lst_arr)
lst_arr = [int(x) for x in lst_arr]
t = max(lst_arr)
count = min(lst_arr)
lst_arr = [str(x) for x in lst_arr]
strok = ' '.join(lst_arr)
arr = [[]]
temp = 0
while count <= t:
    reg = ' ' + str(count) + ' '
    if re.search(reg, strok) != None:
        arr[temp].append(count)
    else:
        temp += 1
        arr.append([])
    count += 1
max_len = len(arr[0])
max_ind = 0
for i in range(len(arr)):
    if max_len < len(arr[i]):
        max_len = len(arr)
        max_ind = i
result = [arr[max_ind][0], arr[max_ind][len(arr[max_ind]) - 1]]

print('Максимальная последовательность:')
print(result)