# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).
quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('В это четверти могут распологаться точки с координатами Х больше 0 и Y больше 0.')
elif quarter == 2:
    print('В это четверти могут распологаться точки с координатами Х меньше 0 и Y больше 0.')
elif quarter == 3:
    print('В это четверти могут распологаться точки с координатами Х меньше 0 и Y меньше 0.')
elif quarter == 4:
    print('В это четверти могут распологаться точки с координатами Х больше 0 и Y меньше 0.')
else:
    print('Вы ввели значение не соответствующее заданию, введите значение в диапазоне от 1 до 4!')
 