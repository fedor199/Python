# Задание 5
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв

print('Введите две буквы')
char1 = input('Введите первую букву: ')
char2 = input('Введите вторую  букву: ')

dig1 = ord(char1) - 96
dig2 = ord(char2) - 96
dig3 = abs(dig1 - dig2) - 1

print(f'Первая буква стоит на {dig1} месте а алфавите')
print(f'Вторая буква стоит на {dig2} месте в алфавите')
print(f'Между ними {dig3} буквы')
