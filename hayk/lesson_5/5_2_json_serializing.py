# сериализация - перевод строчного формата в другой язык

import json

# тройные кавычки позволяют переносить строки в строке '''
data = '''
[
    {
        "id": 1,
        "name": "Леша"
    },
    {
        "id": 2,
        "name": "Паша"
    },
    {
        "id": 3,
        "name": "Ксюша"
    }
]
'''
# сериализация - преобразовуем json в python => json.loads для обработки
lst_data = json.loads(data)

# добавим нового пользователя
new_user = {
    'id': 4,
    'name': 'Margulis'
}

# def new_user () 
#     {
#     'id': 4,
#     'name': 'Margulis'
# }

lst_data.append(new_user)

print(data)
print('С█▓ ' * 13)
print()
print(lst_data)

# преобразование обратно в json => json.dumps
new_data = json.dumps(lst_data, ensure_ascii=False, indent='\t') # ensure_ascii=False => отменить преобразование кириллицы в юникод | indent='\t' => добавляет табуляцию как отступ
print()
print('_- ' * 18)
print()
print(new_data)