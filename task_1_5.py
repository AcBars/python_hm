# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева 
# направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 1



from my_functions import rndint_array

array_2 = []
array_2.append(rndint_array(4, 0, 10))
array_2.append(rndint_array(4, 0, 10))
print('До сортировки.')
for i in range(2):
    print(array_2[i])
count = 0
count_1 = 1
while count < len(array_2[0]) * 2:
    for i  in range(2):
        for j in range(1, len(array_2[i])):
            if array_2[i][j - 1] > array_2[i][j]:
                temp = array_2[i][j - 1]
                array_2[i][j - 1] = array_2[i][j]
                array_2[i][j] = temp
        if i == 1:
            if array_2[i - 1][j] > array_2[i][0]:
                temp = array_2[i - 1][j]
                array_2[i - 1][j] = array_2[i][0]
                array_2[i][0] = temp     
    count += 1
print('После сортировки.')
for i in range(2):
    print(array_2[i])
        
