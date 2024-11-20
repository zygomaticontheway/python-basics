

# переменная __name__ равна __main__ когда выполняется главный файл,
# если __name__ равняется имени файла, то это выполнение не 

# from time import sleep

# print()
# sleep(10)

# print(dir(sleep))


# __all__ = [ #список объектов которые будут импортированы при использовании *
#     'email' 
# ]

token = '123123asdmsam'
email = 'asd@sdfdf.ff'

# проверочное условие заущен ли файл как главный напрямую или через вызов (импорт)
def main():
    print('__name__ variable of the config.py module \n', __name__)

if __name__ == '__main__': #точка входа в скрипт если файл исполняется как основной
    main()


