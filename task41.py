# Задание 2
# Написать два алгоритма нахождения i-го по счёту простого числа

import cProfile


# 1. Без использования «Решета Эратосфена».
def not_sieve(n):
    ratio = n * 100
    lst = [None, 2]
    count = 0
    for i in range(3, ratio + 1, 2):
        mark = 0
        for j in range(3, ratio + 1, 2):
            if j < i:
                if i % j == 0:
                    mark = 1
                    break
        if mark == 0:
            lst.append(i)
            count += 1
        if count == n:
            break
    return lst[count]

# 100 loops, best of 3: 29 msec per loop - 100
# 10 loops, best of 3: 2.95 sec per loop - 1000
# 1 loops, best of 3: 305 sec per loop - 10000

#cProfile.run('not_sieve(10000)')
# 1    0.030    0.030    0.030    0.030 task41.py:8(not_sieve) - 100
# 1    2.995    2.995    2.996    2.996 task41.py:8(not_sieve) - 1000
# 1   312.763  312.763  312.773  312.773 task41.py:8(not_sieve)- 10000


# 2. С использованием «Решета Эратосфена».
def sieve(n):
    ratio = n * 100
    array = [0] * ratio
    for i in range(ratio):
        array[i] = i
    array_simple = [None, ]
    m = 2
    count = 0
    while m <= ratio:
        if array[m] != 0:
            array_simple.append(array[m])
            count += 1
            if count == n:
                break
            for j in range(m, ratio, m):
                array[j] = 0
        m += 1
    return array_simple[count]

# 100 loops, best of 3: 2.5 msec per loop - 100
# 100 loops, best of 3: 30.8 msec per loop - 1000
# 100 loops, best of 3: 399 msec per loop - 10000

# cProfile.run('sieve(10000)')
# 1    0.004    0.004    0.004    0.004 task41.py:28(sieve) - 100
# 1    0.030    0.030    0.030    0.030 task41.py:28(sieve) - 1000
# 1    0.388    0.388    0.389    0.389 task41.py:28(sieve) - 10000

# Выводы.
# Мой вариант реализации функции без использования «Решета Эратосфена» оказался очень медленным и обладает
# сложностью  O(n ** 2). Значительно быстрей работает функция  с использованием «Решета Эратосфена», сложность данного
# алгоритма  можно определить как O(n * log(log n)).
