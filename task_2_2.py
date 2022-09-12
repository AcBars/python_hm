# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def multip_list (number):
    
    list_multip = []
    for i  in range(number):
        list_multip.append(i + 1)
    for i  in range(number):
        if i == 0:
            list_multip[i] = 1
        else:
            list_multip[i] = (i + 1) * list_multip[i - 1]
    return list_multip


number = int(input('Введите натуральное число: '))
print(multip_list (number))
