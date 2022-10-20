import random
def rndint_array(len_array, min_el=-100, max_el=101):
    """The function creates a list consisting of int numbers of a given length.
    By default, the list items are set from -100 to 100.
    You can additionally specify the maximum and minimum values of a list item."""
    arr = []
    for _ in range(0, len_array):
        arr.append(random.randrange(min_el, max_el))
    return arr

def rndfloat_array(len_array, dec_places=3, min_el=-100.000, max_el=101.000):
    """The function creates a list consisting of floating-point numbers of a given length.
        By default, the list items are set in the range from -100 to 100.
        You can additionally specify the maximum and minimum values of the list item and the number of decimal places."""
    arr = []
    for _ in range(0, len_array):
        arr.append(round(random.uniform(min_el, max_el), dec_places))
    return arr

def rounding(numeric_list_int):
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
    return numer_temp

def con_nuber(numer_temp):
    result = 0
    for i in range(len(numer_temp)):
        result = result + numer_temp[i] * 10 ** (len(numer_temp) - i -1)
    return result

def check_numberint (number):
    """Проверка введенного числа, вводит ли ползователь int?"""
    while type: 
        try:
            number = int(number)      
            return number
        except ValueError:
            print('Вы ввели не целое число! ')
            number = input('Введите целое число: ')
            
def check_numberfloat (number):
    """Проверка введенного числа, вводит ли ползователь float?"""
    while type: 
        try:
            number = float(number)      
            return number
        except ValueError:
            print('Вы ввели не вещественное число! ')
            number = input('Введите вещественное число: ')
