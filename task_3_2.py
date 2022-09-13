# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



from my_functions import rndint_array

def product_numbers(arr):
    """This is a function that will find the product of pairs of numbers in the list."""
    arr_result = []
    for i in range(0, (len(arr) // 2)):
        if i < len(arr) // 2:
            arr_result.append(arr[i] * arr[len(arr) - i - 1])
    if len(arr) % 2 > 0:
        arr_result.append(arr[len(arr) // 2] ** 2)
    return arr_result

len_list = int(input('Введите длину списка чисел: '))
initial_list = rndint_array(len_list)

print(f'{initial_list} => {product_numbers(initial_list)}')