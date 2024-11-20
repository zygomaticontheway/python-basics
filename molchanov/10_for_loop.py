
children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Bubnov_2015']

names = []

for child_name in children:
    # arbuzov_2000 > arbuzov, 2000
    surname = child_name.split('_')[0].title() #разделили по _, взяли первый элемент и сделали его с заглавной буквы, но если такое будет то следующая проверка на бакву "а" не отработает изза регистра

    # break
    # continue

    if surname.startswith('a'): # проверка на наличие имен начинающихся с "а" и пропуск таких имен без прерывания цикла
        continue

    # surname = surname.title() применили методом title в функции
    names.append(surname)

print(names)


# break - прерывает цикл. управление переходит в код после цикла
# continue - пропускает код на текущей итерации и 
#
#
#