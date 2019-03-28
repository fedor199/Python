# Задание 9
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

print('Введите три разных  числа')

dig1 = int(input('Введите первое целое число: '))
dig2 = int(input('Введите второе целое число: '))
dig3 = int(input('Введите третье целое число: '))

if (dig1 > dig2 or dig1 > dig3) and (dig1 < dig2 or dig1 < dig3):
    print(f'Среднее число = {dig1}')
elif (dig2 > dig1 or dig2 > dig3) and (dig2 < dig1 or dig2 < dig3):
    print(f'Среднее число = {dig2}')
else:
    print(f'Среднее число = {dig3}')