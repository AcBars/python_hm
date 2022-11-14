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
    m_con_1 = chek_sign(mult_1)
    m_con_2 = chek_sign(mult_2)
    mult_result = float(m_con_1) * float(m_con_2)
    return mult_result

def dif(dif_1, dif_2):
    d_con_1 = chek_sign(dif_1)
    d_con_2 = chek_sign(dif_2)
    dif_result = float(d_con_1) / float(d_con_2)
    return dif_result

def plus(plus_1, plus_2):
    p_con_1 = chek_sign(plus_1)
    p_con_2 = chek_sign(plus_2)
    plus_result = float(p_con_1) + float(p_con_2)
    return plus_result

def minus(minus_1, minus_2):
    mi_con_1 = chek_sign(minus_1)
    mi_con_2 = chek_sign(minus_2)
    minus_result = float(mi_con_1) - float(mi_con_2)
    return minus_result

con = input('Введите условие: ')
total_res = chek_sign(con)
print(f'{con}={total_res}')