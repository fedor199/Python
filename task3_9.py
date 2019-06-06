# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

LINES = 4
COLUMNS = 5
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(COLUMNS)] for _ in range(LINES)]
array_min = []

print('Исходная матрица:')
for line in matrix:
    for item in line:
        print(f'{item:>5}', end=' ')
    print()

print('Минимальные элементы столбцов матрицы:')
for j in range(COLUMNS):
    my_min = matrix[0][j]
    for i in range(LINES):
        if matrix[i][j] < my_min:
            my_min = matrix[i][j]
    print(f'{my_min:>5}', end=' ')
    array_min.append(my_min)

my_max = array_min[0]
for item in array_min:
    if item > my_max:
        my_max = item
print()
print(f'Число {my_max} максимальный элемент среди минимальных элементов столбцов матрицы')
