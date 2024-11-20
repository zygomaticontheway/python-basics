

person = {
    'name': 'vasya', 
    'surname': 'pupkin', 
    'email': 'test@gmail.com'
    }

d = dict(name = 'petr', tel = '1234')

# tel = person.setdefault('tel', '12345123')
# print(tel)
# print()
# print(person)

# for item in person.items():
#     print(item)

# # то же самое что и выше
# for key, value in person.items():
#     print(key, value)

# a, b = [1, 2]
# print(a)
# print(b)

new = {'name': 'dima', 'tel': '123q'}

person.update(new)
# same as above
#  person.update(name = 'dimas', tel = '123zxc')
# print(person)

# тип данных None

def a():
    print('hi world')
    return None #none писать не обязательноэто и так по умолчанию делается

result = a()
print(result)