# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 

#     1+2*3 => 7; 

#     (1+2)*3 => 9;

import re

con = input('Введите выражение: ')

while con.find('*') > 0:
    reg = r"\d+\*\d+\.\d+|\d+\*\d+|\d+\.\d+\*\d+\.\d+|\d+\.\d+\*\d+"
    mult = re.search(reg, con)
    mult = mult.group()
    mult_arr = mult.split('*')
    temp = str(float(mult_arr[0]) * float(mult_arr[1]))
    con = re.sub(reg, temp, con, count=1)
while con.find('/') > 0:
    reg = r"\d+\/\d+\.\d+|\d+\/\d+|\d+\.\d+\/\d+\.\d+|\d+\.\d+\/\d+"
    mult = re.search(reg, con)
    mult = mult.group()
    mult_arr = mult.split('/')
    temp = str(float(mult_arr[0]) / float(mult_arr[1]))
    con = re.sub(reg, temp, con, count=1)
while con.find('+') > 0:
    reg = r"\d+\+\d+\.\d+|\d+\+\d+|\d+\.\d+\+\d+\.\d+|\d+\.\d+\+\d+"
    mult = re.search(reg, con)
    mult = mult.group()
    mult_arr = mult.split('+')
    temp = str(float(mult_arr[0]) + float(mult_arr[1]))
    con = re.sub(reg, temp, con, count=1)
if con.find('-') == 0:
    mult_arr = con.split('-')
    total = -1 * float(mult_arr[1])
    for i in range(2, len(mult_arr)):
        total -= float(mult_arr[i])
        con = total
elif con.find('-') > 0:
    mult_arr = con.split('-')
    total = float(mult_arr[0])
    for i in range(1, len(mult_arr)):
        total -= float(mult_arr[i])
        con = total
print(con)