# Задание:
# Получить 2 целых числа вводом и вывести наибольшее
# Если равны, то вывести об этом сообщение

value_1 = int(input('укажите 1 число:'))
# int_value_1 = int(value_1)

value_2 = int(input('укажите 2 число:'))
# int_value_2 = int(value_2)

if value_1 > value_2:
    print(value_1)
elif value_1 < value_2:
    print(value_2)
else:
    print('числа равны')