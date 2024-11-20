
# value = input('укажите целое число:')
# int_value = int(value)

# if int_value > 0:
#     print('положительное число')
# elif int_value < 0:
#     print('отрицательное число')
# else:
#     print('ты правда ввел ноль?')
    
# от 0 до 6 это малыш
# от 7 до 12 это ребенок
# от 13 до 17 это подросток
# от 18 до 30 это молодой чел
# от 31 до 60 это взрослый
# от 61 до 150 это пожилой
# больше 150 ошибка ввода

value = input('укажите ваш возраст:')
age = int(value)

# if age < 0 and age >= 151:
#     print('ошибка ввода')
if not (age >= 0 and age < 151):
    print('ошибка ввода')
elif age >=0 and age <=6:
    print('малыш')
elif age <= 12:
    print('ребенок')
elif age <= 17:
    print('подросток')
elif age <= 30:
    print('молодой чел')
elif age <= 60:
    print('взрослый')
else:
    print('пожилой')