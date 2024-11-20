
# написать функцию кот получает в качестве аргумента путь до
# json файла и возвращает его в текстовом виде

import json

def read_json (path):
    with open(path, 'r', encoding='UTF-8') as f:
        return json.loads(f.read())
    
    
data = read_json('/Users/zygomactic/Study_Py/hayk/lesson_5/5_4_data.json') 
print(data)

# написать функцию кот получает в качестве аргумента путь до
# json файла и питоновский список словарей и записывает json с данными в файл
def write_json (path, data_file):
    with open(path, 'w', encoding='UTF-8') as f:
        data_file = json.dumps(data_file, ensure_ascii=False, indent='\t')
        f.write(data_file)

new_product = {
    "id": 4,
    "title": "Сноуборд",
    "price": 20000
}

# добавление элемента в первоначальный словарь
data.append(new_product)
write_json ('5_5_data.json', data)
