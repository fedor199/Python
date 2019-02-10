# Задание 1
# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только
# из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке

import hashlib


def number_subs(string):
    dict_hash = {}
    h_string = hashlib.sha1(string.encode('utf-8')).hexdigest()
    dict_hash[h_string] = True
    count = 0
    for i in range(len(string)):
        for j in range(len(string) - i):
            h_string = hashlib.sha1(string[i:i + j + 1].encode('utf-8')).hexdigest()
            if dict_hash.get(h_string):
                continue
            else:
                dict_hash[h_string] = True
                count += 1
    return count


my_str = input('Введите строку: ')
print(f'В строке {my_str} количество различных подстрок: {number_subs(my_str)}')
