# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
 



from my_functions import rndfloat_array

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

def con_nuber(numeric_list_int):
    numer_temp = []
    count = 0
    for i in range(0, (len(numeric_list_int) - 2)):
        if numeric_list_int[i] == numeric_list_int[i + 1] == numeric_list_int[i + 2]:
            
            for j in range(0, i):
                if numeric_list_int[i + 2] >= 5 and j == i - 1:
                    numer_temp.append(numeric_list_int[j] + 1)
                else:    
                    numer_temp.append(numeric_list_int[j])
            break
    result = 0
    for i in range(len(numer_temp)):
        result = result + numer_temp[i] * 10 ** (len(numer_temp) - i -1)
    return result

list_number = rndfloat_array(3, 2)
print(list_number)
result = con_nuber(fractional_part(list_number))
print(result)