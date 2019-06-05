# Во втором массиве сохранить индексы четных элементов первого массива

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_even = []

print(f'В данном массиве: {array}')

for i, item in enumerate(array):
    if item % 2 == 0:
        array_even.append(i)

print(f'Индексы четных элементов: {array_even}')
