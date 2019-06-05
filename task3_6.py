# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# Если максимальные или минимальные элементы повторяются, сумма элементов считается между первыми встречающемися.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
index_min = 0
index_max = 0
my_sum = 0

print(f'Исходный массив: {array}')

my_min = array[0]
my_max = array[0]
for i, item in enumerate(array):
    if item < my_min:
        my_min = item
        index_min = i
    elif item > my_max:
        my_max = item
        index_max = i
if index_max > index_min:
    for i in range(index_min + 1, index_max):
        my_sum += array[i]
else:
    for i in range(index_max + 1, index_min):
        my_sum += array[i]

print(f'Минимальный элемент: {my_min}, максимальный элемент: {my_max}')
print(f'Полученная сумма: {my_sum}')
