# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

from collections import namedtuple

Point = namedtuple('Point', ['name', 'quarter1', 'quarter2', 'quarter3', 'quarter4'])
lst = []
low = []
high = []
my_sum = 0

number = int(input('Введите количество предприятий: '))

for item in range(number):
    name = input('Введите название предприятия: ')
    quarter1 = int(input('Введите прибыль 1-го квартала: '))
    quarter2 = int(input('Введите прибыль 2-го квартала: '))
    quarter3 = int(input('Введите прибыль 3-го квартала: '))
    quarter4 = int(input('Введите прибыль 4-го квартала: '))
    lst.append(Point(name, quarter1, quarter2, quarter3, quarter4))
    my_sum += quarter1 + quarter2 + quarter3 + quarter4

my_sum = my_sum / number

for i in range(number):
    if lst[i].quarter1 + lst[i].quarter2 + lst[i].quarter3 + lst[i].quarter4 > my_sum:
        high.append(lst[i].name)
    if lst[i].quarter1 + lst[i].quarter2 + lst[i].quarter3 + lst[i].quarter4 < my_sum:
        low.append(lst[i].name)

print('Предприятия чья прибыль выше среднего:', end=' ')
for item in high:
    print(f'{item}', end=' ')
print()
print('Предприятия чья прибыль ниже среднего:', end=' ')
for item in low:
    print(f'{item}', end=' ')
