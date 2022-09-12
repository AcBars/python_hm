# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш",
# "кабак". А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны
# читалось одинаково, но есть одно "но". Если перевернутое число не равно исходному,
# то они складываются и проверяются на палиндром еще раз. Это происходит до тех пор,
# пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.



def check_number (number):
    while type: 
        try:
            number = int(number)
            if number < 0:
                print('Вы вели отрицательное число!')
                number = check_number(input('Введите положительное натуральное число: '))
            

            return number
        except ValueError:
            print('Вы ввели значение не отвечающее заданию! ')
            number = input('Введите положительное натуральное число: ')
        
def polydrome_numbers (number):

    temp = str(number)
    temp_list = list(temp)
    temp_list.reverse()
    temp_2 = int("".join(map(str,temp_list)))
   
    print(f'{number}=={temp_2}={number == temp_2}')
    if number != temp_2:
        number += temp_2
      
        polydrome_numbers (number)



polydrome_numbers (check_number (input('Введите положительное натуральное число: ')))
