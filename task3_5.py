# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Если максимальный отрицательный элемент встречается несколько раз, выводится первая встречающееся позиция в массиве.

import random

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
my_max = 0
index_max = 0

print(f'Исходный массив: {array}')

for i in range(SIZE):
    if array[i] < my_max:
        my_max = array[i]

if my_max < 0:
    for i, item in enumerate(array):
        if item < 0:
            if item > my_max:
                my_max = item
                index_max = i
    print(f'Максимальный отрицательный элемент: {my_max}, его позиция: {index_max}')
else:
    print ('Нет отрицальных чисел')
