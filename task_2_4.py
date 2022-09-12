# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

from random import randint
import time



def randomaizer(max):

    numbers_1 = int((time.time_ns() - (time.time_ns()/10))%1000)
 
    # while max <= numbers:
    #     numbers //= 10
 

    return numbers_1
print(randomaizer(100)) 

def rnd_array(lengs_array):
    array = []
    for i in range(lengs_array):
        array.append(randomaizer(100))
        #array.append(randint(0, 10))
    return array


def dictionary(array):
    
    for j in range(100):
        count = 0
        for i in range(len(array)):
            if array[i] == j:
                count += 1
        if count > 0:
            print(f'Элемент "{j} встречается - {count} раз или {count/len(array) * 100}%')

array = rnd_array(100)
dictionary(array)
print(array)