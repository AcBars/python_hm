# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.




def rle_compression(text):
    arr = list(text)
    arr.append('')
    result = []
    i = 1
    while i < len(arr):
        if arr[i - 1] != arr[i]:
            result.append(arr[i - 1])
            i += 1
        else:
            temp = i-1
            count = 1
            while arr[temp] == arr[i]:
                i += 1
                count += 1
            result.append(arr[temp])
            result.append(':')
            result.append(str(count))
            i += 1
    return result
with open('python_hm/task_5_2.txt', 'r') as f:
    text = f.read()
arr = rle_compression(text)
res_text = ''.join(arr)
f = open('python_hm/task_ex_5_2.txt', 'w')
f.write(res_text)
f.close()