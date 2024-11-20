
# написать функцию кот получает путь до файла и строку в качестве аргумента
# и вписывает указанную строку в файл

# def add_row (path, string):
#     with open(path, 'a', encoding='UTF-8') as f:
#         f.write('\n' + string)

# add_row ('test.txt', 'добавляемая строка')

# написать функцию кот получает
# аргумент - путь до файла и считывает его содержимое
# считанное содержимое функция должна возвращать

def path_file (path):
    with open(path, 'r', encoding='UTF-8') as f:
        f_path = f.read()
        # print(f_path)
    return f_path

print(path_file ('test.txt'))

