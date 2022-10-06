# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные
# буквы фамилии тех студентов, которые имеют средний балл более «4».

# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

#with open("python_hm/text_4_3.txt", "r") as f:



with open('python_hm/text_4_3.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
print(text)

for i in range(len(text)):
    temp_list = text[i].split()
    temp = int(temp_list[2])
    if temp == 5:
        new_list = list(temp_list[0])
        
        for i in range(1, len(new_list)):
            new_list[i] = chr(ord(new_list[i]) - 32)
        
        temp_list[0] = ''.join(new_list)
        new_list = list(temp_list[1])
        
        for i in range(1, len(new_list)):
            new_list[i] = chr(ord(new_list[i]) - 32)
        
        temp_list[1] = ''.join(new_list)
        temp_list = ','.join(temp_list)
        print(temp_list)

# print(text[0].split())
# print(chr(ord('Б') + 32))
# s = ['Артем']
# list(s)
# print(s)