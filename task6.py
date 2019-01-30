# Задание 1
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Анализируется задача № 8 из домашнего задания № 2.
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
#
# Комментарий:
# Анализируется выделение памяти в 3-х реализациях функции подсчета введенной с клавиатуры цифры в введенной
# последовательности чисел. Память в теле программы, в которой осуществляется ввод данных  и вывод результата
# программы, не анализируется, так как тело программы не меняется.
# Версия Python 3.6.0, ОС Windows 7 64-х разрядная
#
# Выводы:
# Наименьшее количество памяти под переменные использует функция "cycle_count"
# Наибольшее количество памяти под переменные использует функция "cycle_count_lst", в связи с использованием списка.
# Пример:
# Введите цифру: 5
# Введите число: 123456543
# Под переменные в функции "cycle_count" выделено 80 байт памяти
# Под переменные в функции "cycle_count_lst" выделено 364 байт памяти
# Под переменные в функции "count_func" выделено 84 байт памяти


import sys

RAZ = 10


def my_decorator(count_):
    def show_size():
        sum_ = 0
        res = count_(dig, cf)
        for key in res:
            if hasattr(res[key], '__iter__'):
                for item in res[key]:
                    sum_ += sys.getsizeof(item)
            else:
                sum_ += sys.getsizeof(res[key])
        print(f'Под переменные в функции "{count_.__name__}" выделено {sum_} байт памяти')
        return sum_
    return show_size


def cycle_count(dig, cf):
    sm = 0
    while True:
        if dig % RAZ == cf:
            sm += 1
        dig = dig // RAZ
        if dig == 0:
            break
    return locals()


def cycle_count_lst(dig, cf):
    sm = 0
    array = [int(x) for x in str(dig)]
    for item in array:
        if item == cf:
            sm += 1
    return locals()


def count_func(dig, cf):
    sm = [int(x) for x in str(dig)].count(cf)
    return locals()


cnt = int(input('Введите количество вводимых чисел: '))
cf = int(input('Введите цифру: '))
sm = 0
for i in range(cnt):
    dig = int(input('Введите число: '))
    d = cycle_count(dig, cf)
    sm += d['sm']
    my_size = my_decorator(cycle_count)
    my_size()
    my_size = my_decorator(cycle_count_lst)
    my_size()
    my_size = my_decorator(count_func)
    my_size()
print(f'Цифра {cf} встречается {sm} раза')