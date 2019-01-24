# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

from collections import deque

digit1 = input('Введите первое шестнадцатеричное число: ')
digit2 = input('Введите второе шестнадцатеричное число: ')
deq1 = deque([])
deq2 = deque([])
deq_sum = deque([])
deq_inc = deque([])
my_sum = str()
my_inc = str()
d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
d_r = {10 : 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
spam = 0
k = 0

array1 = [_ for _ in digit1]
array2 = [_ for _ in digit2]

# Создание очередей с преобразование символов в цифры
for key in array1:
    if key in d:
        deq1.appendleft(d[key])
    else:
        deq1.appendleft(int(key))
for key in array2:
    if key in d:
        deq2.appendleft(d[key])
    else:
        deq2.appendleft(int(key))

# Приведение очередей к одинаковому количеству элементов для сложения
if len(deq1) > len(deq2):
    for _ in range(len(deq1) - len(deq2)):
        deq2.append(0)
if len(deq1) < len(deq2):
    for _ in range(len(deq2) - len(deq1)):
        deq1.append(0)

# Сложение i элементов очередей
for i in range(len(deq1)):
    sum_ = deq1[i] + deq2[i]
    if sum_ + spam > 15:
        deq_sum.appendleft((sum_ + spam) % 16 )
        spam = (sum_ + spam) // 16
    else:
        deq_sum.appendleft(sum_ + spam)
        spam = 0
    if i == len(deq1) - 1 and spam != 0:
        deq_sum.appendleft(spam)
        spam = 0

# Создание очередей с преобразованием символов в цифры
deq1.clear()
deq2.clear()
for key in array1:
    if key in d:
        deq1.appendleft(d[key])
    else:
        deq1.appendleft(int(key))
for key in array2:
    if key in d:
        deq2.appendleft(d[key])
    else:
        deq2.appendleft(int(key))

# Создание двухмерного списка для  умножения элементов очередей
ln1 = len(deq1)
ln2 = len(deq2)
matrix = [[0 for _ in range(ln1 + ln2)] for _ in range(ln2)]

# Умножение элементов очередей и запись результата в двухмерный список
for x2 in range(ln2):
    for x1 in range(ln1):
        if deq2[x2] == 0:
            spam = 0
            continue
        inc_ = deq2[x2] * deq1[x1]
        if inc_ + spam > 15:
            matrix[x2][x1 + k] = (inc_ + spam) % 16
            spam = (inc_ + spam) // 16
        else:
            matrix[x2][x1 + k] = inc_ + spam
            spam = 0
        if x1 == ln1 - 1 and spam != 0:
            matrix[x2][x1 + k + 1] = spam
            spam = 0
    k += 1

# Сложение i,j элементов двухмерного списка
for j in range(ln1 + ln2):
    sum_ = 0
    for i in range(ln2):
        sum_ += matrix[i][j]
    if sum_ + spam > 15:
        deq_inc.appendleft((sum_ + spam) % 16 )
        spam = (sum_ + spam) // 16
    else:
        deq_inc.appendleft(sum_ + spam)
        spam = 0
    if j == ln1 + ln2 - 1 and spam != 0:
        deq_inc.appendleft(spam)
        spam = 0

# Вывод результатов с преобразованием цифр в символы
for key in deq_sum:
    if key in d_r:
        my_sum += str(d_r[key])
    else:
        my_sum += str(key)
print(f'Сумма шестнадцатеричных чисел:  {my_sum}')
for key in deq_inc:
    if key in d_r:
        my_inc += str(d_r[key])
    else:
        my_inc += str(key)
print(f'Произведение шестнадцатеричных чисел:  {my_inc}')