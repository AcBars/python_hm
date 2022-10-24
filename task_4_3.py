# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в
# файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = str(input('Введите коэфициент k: '))
k_1 = randint(0, 101)
k_2 = randint(0, 101)
k_3 = randint(0, 101)
if k_1 == 0:
    polynomial_list = [k, '+', k_2, 'x', '+', k_3]
elif k_2 == 0:
    polynomial_list = [k_1, 'x^', k, '+', k_3]
elif k_3 == 0:
    polynomial_list = [k_1, 'x^', k, '+', k_2, 'x']
else:
    polynomial_list = [k_1, 'x^', k, '+', k_2, 'x', '+', k_3]
result = ''
for i in range(len(polynomial_list)):
    result = result + str(polynomial_list[i])
print(result)
