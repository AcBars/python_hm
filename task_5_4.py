# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.

# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9


import re


def chek_polyn(lst):
    '''Checking the correctness of the spelling of the polynomial
    Проверка правильности написания многочлена'''
    temp = re.sub(' ', '', lst)
    reg = r'[A-Za-wy-zА-Яа-я]|/|\.|\+\*|\*\+|\d\^|=|!|\W\^'
    t = re.search(reg, temp)
    while t != None:
        print('Вы ввели не многочлен или он не соответствует примеру. Есть лишние знаки или нарушен их порядок')
        lst = input('Введите многочлен согласно примера: 5* x^3+ 2*x ^2 +6')
        temp = re.sub(' ', '', lst)
        t = re.search(reg, temp)
    return temp
    
def polyn_list(polynom):
    '''Reduction of a polynomial to a list of lists where the element with index 0 is the value of the coefficient,
    and the element with index 1 is the value of the degree of the order of the polynomial.
     Приведение многочлена к списку  списков где элемент с индексом 0 это значение коэффициента,
     а элемент с индексом 1 это значение  степени челена многочлена.'''
    result = re.split('\+', polynom)
    for i in range(1, len(result)):
        result[i] = '!+' + result[i]
    temp = ''.join(result)
    temp = re.split('\-', temp)
    for i in range(1, len(temp)):
        temp[i] = '!-' + temp[i]
    temp = ''.join(temp)
    temp = re.split('!', temp)
    for i in range(len(temp)):
        temp[i] = re.split('\*x\^|\*x', temp[i])
    temp_2 = ''
    for i in range(len(temp)):
        if len(temp[i]) < 2:
            temp[i].append('0')
        if temp[i][1] == temp_2:
            temp[i][1] = '1'
        temp[i][0] = int(temp[i][0])
        temp[i][1] = int(temp[i][1])
    ord_list(temp)
    return temp

def ord_list(lst):
    '''The function of adding elements of a two-dimensional array
    with the same values of elements under the index 1.
    Функция  сложения элементов двухмерного массива с одинаковыми
    значениями элементов под индексом 1. '''
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][1] == lst[j][1]:
                lst[i][0] += lst[j][0]
                lst[j][0] = 0
    temp = []
    for i in range(len(lst)):
        if lst[i][0] == 0:
            temp.append(i)
    temp_1 = len(temp)
    for i in range(temp_1 - 1, -1, -1):
        lst.pop(temp[i])
    return lst

def lst_sort(lst):
    '''Sorting a two-dimensional list in ascending order
    of the second element in a nested list
    Сортировка двухмерного списка по возрастанию второго
    элемента во вложенном списке'''
    count = 1
    while count <= len(lst):
        for i in range(len(lst) - 1):
            if lst[i][1] < lst[i + 1][1]:
                temp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = temp
        count += 1
    return lst    
        
def lst_polyn(lst):
    '''Reducing a list of lists to str as a polynomial
    Приведение списка списков к str в виде многочлена'''
    for i in range(1, len(lst)):
        if lst[i][0] > 0:
            lst[i][0] = '+' + str(lst[i][0])
    for i in range(len(lst)):
        if lst[i][1] > 1:
            lst[i][0] = str(lst[i][0])
            lst[i][1] = str(lst[i][1])
            lst[i] = '*x^'.join(lst[i])
        elif lst[i][1] == 1:
            lst[i].pop(1)
            lst[i][0] = str(lst[i][0]) + '*x'
            lst[i] = ''.join(lst[i])
        else:
            lst[i].pop(1)
            lst[i][0] = str(lst[i][0])
            lst[i] = ''.join(lst[i])
    lst = ''.join(lst)    
    return lst


temp = polyn_list(chek_polyn(input('Введите первый многочлен согласно примера: 5* x^3+ 2*x ^2 +6: ')))
temp.extend(polyn_list(chek_polyn(input('Введите второй многочлен согласно примера: 5* x^3+ 2*x ^2 +6: '))))
temp = lst_polyn(lst_sort(ord_list(temp)))

print(temp)