# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых
# множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from my_functions import check_numberint

def prime_list(number):
    number_list = [2]
    for i in range(3, number):
        temp = prime_number(i)
        if temp != None:
            number_list.append(temp)
    return number_list
    
  
def prime_number(a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        return a
    return
def mult_numb(number):
    list_nub = prime_list(number)
    result_list = []
    for i in range(len(list_nub)):
        if number % list_nub[i] == 0:
            result_list.append(list_nub[i])
    return result_list
number = int(check_numberint (input('Введите число: ')))
print(mult_numb(number))