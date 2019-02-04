# Задание 1
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
# В качестве улучшения алгоритма используется переменная-флаг для сокращения ненужных проходов и уменьшено количество итераций в цикле.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100


def bubble_sort(array):
    n = 1
    while n < len(array):
        check = 0
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                check = 1
        if check == 0:
            break
        n += 1


array = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]
print('Исходный массив:')
print(array)
bubble_sort(array)
print('Отсортированный массив:')
print(array)
