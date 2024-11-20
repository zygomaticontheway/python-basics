
# movie = 'Titanic, britanic, aurora'
# rating = 100

# print()

# result = f'movie: "{movie}", rating: {rating}'
# print(result)

# print()

movie = 'alien'
# rating = 200

# result = f'movie: "{movie}", rating: {rating}'
# print(result)


def greet (message, name = 'lord'):
    # print('hello ', name)
    result = f'{message} {name}'
    return result


# сопоставление аргументов в функции по позиции
# позиционный аргумент
g = greet('hello', 'world').title() #если указать в функции return, то результат нужно ловить в переменную
print(g)

# сопоставление аргументов в функции по именам
# именованный аргумент
greet(message='hello', name='world') 

# сопоставление аргументов со значением по умолчанию
# значение по умолчанию присваивается при объявлении переменных функции
greet('hello') 

