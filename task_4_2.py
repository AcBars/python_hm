# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from my_functions import rndint_array
new_list = rndint_array(100, 0, 10)

def no_repetitions(numder_list):
    """Creates a new list based on the list without repeating the list items"""
    result = []
    for i in range(len(numder_list)):
        temp = 0
        for j in range(len(result)):
            if result[j] == numder_list[i]:
                temp += 1
        if temp == 0:
            result.append(numder_list[i])
    return result
print(new_list)       
print(no_repetitions(new_list))