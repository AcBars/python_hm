# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
 



from my_functions import rndfloat_array

list_number = [4.07, 5.1, 8.2444, 6.98]
# list_number = rndfloat_array(3, 2)
# print(list_number)
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
for i in range(0, len(numeric_list_int)):
    if numeric_list_int[i] == numeric_list_int[i + 1] == numeric_list_int[i + 2]:

print(numeric_list)