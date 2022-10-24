# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в
# файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint



k = int(input('Введите коэфициент k: '))
polynomial_list = list()
for i in range(k + 1):
    temp = randint(0, 100)
    if temp !=0:
        if k-i == 1:
            polynomial_list.append(str(temp) + '*x+')
        elif k-i == 0:
            polynomial_list.append(str(temp))
        else:
            polynomial_list.append(str(temp) + '*x^' + str(k-i) + '+')
    
result = ''
for i in range (len(polynomial_list)):
    result += polynomial_list[i]
with open('python_hm/task_4_3.txt', 'w') as f:
    f.write(result)


