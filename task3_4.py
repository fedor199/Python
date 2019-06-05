# Определить, какое число в массиве встречается чаще всего.
# Если несколько чисел встречаются чаще всего, выводится первое встречающееся число.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_count = 0
max_number = 0

print(f'Исходный массив: {array}')

for i in range(SIZE):
    num = array[i]
    counter = 0
    for j in range(SIZE):
        if num == array[j]:
            counter += 1
    if counter > max_count:
        max_count = counter
        max_number = num

print(f'Число {max_number} встречается в массиве чаще всего')