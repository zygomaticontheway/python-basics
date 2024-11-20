# написать функцию append_to_file кот принимает 2 аргумента
# путь до файла и добавляемую строку
# строка добавляется с новой строки

from pyparsing import line


def append_to_file (path, string):
    with open(path, 'a', encoding='UTF-8') as f:
        f.write('\n' + string)

append_to_file('test1.txt', 'добавляемая строка')