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
        list(temp_list[0])
        print(temp)

# print(text[0].split())
# print(ord('Б'))
# s = ['Артем']
# list(s)
# print(s)