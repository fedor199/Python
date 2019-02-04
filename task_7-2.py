# Задание 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50


def merge_array(first,second):
    final = []
    while len(first) != 0 and len(second) != 0:
        if first[0] < second[0]:
            final.append(first[0])
            first.remove(first[0])
        else:
            final.append(second[0])
            second.remove(second[0])
    if len(first) == 0:
        final += second
    if len(second) == 0:
        final += first
    return final


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        return merge_array(merge_sort(array[:mid]), merge_sort(array[mid:]))


array = [random.uniform(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]
print('Исходный массив:')
print(array)
array_sort = merge_sort(array)
print('Отсортированный массив:')
print(array_sort)

