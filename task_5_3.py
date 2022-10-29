# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

import re

with open('python_hm/task_in_5_3.txt', 'r', encoding = 'utf_8') as f:
    s = f.read()
reg = r'[А-Яа-я]*абв[А-Яа-я]*|абв[А-Яа-я]*|[А-Яа-я]*абв'
text = re.sub(reg, '', s)
with open('python_hm/task_ex_5_3.txt', 'w', encoding = 'utf_8') as f:
    f.write(text)