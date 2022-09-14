# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
 



from my_functions import rndfloat_array
from my_functions import rounding
from my_functions import con_nuber

# list_number = [4.07, 5.1, 8.2444, 6.98]

def fractional_part(list_number):
    for i, cha in enumerate(list_number):
        list_number[i] %= 1
    remains_min = min(list_number)
    remains_max = max(list_number)
    difference = remains_max - remains_min
    print(difference)

    numeric = str(difference)
    numeric_list = list(numeric)
    numeric_list.remove('.')
    numeric_list.remove('0')
    numeric_list_int = [int(x) for x in numeric_list]
    return numeric_list_int



list_number = rndfloat_array(3, 2)
print(list_number)
result = rounding(fractional_part(list_number))
result = con_nuber(result)
print(result)