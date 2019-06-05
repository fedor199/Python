# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Если максимальные или минимальные элементы повторяются меняются местами первые встречающееся.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
index_min = 0
index_max = 0

print(f'Исходный массив:   {array}')

my_min = array[0]
my_max = array[0]
for i, item in enumerate(array):
    if item < my_min:
        my_min = item
        index_min = i
    elif item > my_max:
        my_max = item
        index_max = i
array[index_min], array[index_max] = array[index_max], array[index_min]

print(f'Минимальный элемент: {my_min}, максимальный элемент: {my_max}')
print(f'Полученный массив: {array}')
