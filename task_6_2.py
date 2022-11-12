# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 

#     1+2*3 => 7; 

#     (1+2)*3 => 9;




def chek_sign(con):
    if i:= con.find('+') >= 0:
        con_1 = con[0:i]
        con_2 = con[i + 1:]
        result = plus(con_1, con_2)
    elif i := con.find('-') >= 0:
        con_1 = con[0:i]
        con_2 = con[i + 1:]
        result = minus(con_1, con_2)
    elif i:= con.find('*') >= 0:
        con_1 = con[0:i]
        con_2 = con[i + 1:]
        result = mult(con_1, con_2)
    elif i:= con.find('/') >= 0:
        con_1 = con[0:i]
        con_2 = con[i + 1:]
        result = dif(con_1, con_2)
    else:
        result = float(con)
    
    return result

def mult(mult_1, mult_2):
    con_1 = chek_sign(mult_1)
    con_2 = chek_sign(mult_2)
    mult_result = float(con_1) * float(con_2)
    return mult_result

def dif(con_1, con_2):
    chek_sign(con_1)
    chek_sign(con_2)
    dif_result = float(con_1) / float(con_2)
    return dif_result

def plus(con_1, con_2):
    chek_sign(con_1)
    chek_sign(con_2)
    plus_result = float(con_1) + float(con_2)
    return plus_result

def minus(con_1, con_2):
    chek_sign(con_1)
    chek_sign(con_2)
    minus_result = float(con_1) - float(con_2)
    return minus_result

con = input('Введите условие: ')
total_res = chek_sign(con)
print(f'{con}={total_res}')


# con = input('Введите условие: ')

# if i:= con.find('*') >= 0:
#     con_1 = con[0:i]
#     con_2 = con[i + 1:]
#     print(f'{con_1}*{con_2}={float(con_1)*float(con_2)}')
# elif i:= con.find('/') >= 0:
#     con_1 = con[0:i]
#     con_2 = con[i + 1:]
#     print(f'{con_1}/{con_2}={float(con_1)/float(con_2)}')