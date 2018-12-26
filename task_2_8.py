# Задание 8
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def count(dig, cf):
    RAZ = 10
    dig1 = dig % RAZ
    if dig == 0:
        return 0
    if dig1 == cf:
        return 1 + count(dig // RAZ, cf)
    else:
        return count(dig // RAZ, cf)

cnt = int(input('Введите количество вводимых чисел: '))
cf = int(input('Введите цифру: '))
sm = 0

for i in range(cnt):
    dig = int(input('Введите число: '))
    sm += count(dig, cf)

print(f'Цифра {cf} встречается {sm} раза')